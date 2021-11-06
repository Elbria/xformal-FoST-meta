#!/bin/bash

##SBATCH --job-name=xformal
##SBATCH --time=1-00:00:00
##SBATCH --mem=40g
##SBATCH --qos=gpu-medium
##SBATCH --exclude=materialgpu00,materialgpu02
##SBATCH --nodelist=clipgpu01
##SBATCH --cpus-per-task=6
##SBATCH --gres=gpu:1
##SBATCH --partition=gpu


export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/fs/clip-xling/projects/semdiv/anaconda3/lib

source ~/.bashrc

conda activate /fs/clip-xling/projects/semdiv/anaconda3/envs/xformal
#export TRANSFORMERS_CACHE=/fs/clip-scratch/xformal-scratch/CACHE_$2
export TRANSFORMERS_CACHE=/fs/clip-divergences/x-formal

# base_models="xlm-roberta-base bert-base-multilingual-cased"
#base_models="xlm-roberta-base bert-base-multilingual-cased"
base_models="xlm-roberta-base"
# base_models="facebook/mbart-large-50"
learning_rate="5e-5"
tune_tasks=regression
test_langs=$1
#output_dir=/fs/clip-scratch/xformal-scratch/models
#run_dir=/fs/clip-scratch/xformal-scratch/runs
output_dir=/fs/clip-divergences/x-formal/models
run_dir=/fs/clip-divergences/x-formal/runs
batch_size=8

for tune_task in $tune_tasks; do

	if [[ $tune_task == binary_classification ]]; then
		epoch=3
	else
		epoch=5
	fi;

	for base_model in $base_models; do
		for test_lang in $test_langs; do
			if [[ $tune_task == binary_classification ]]; then
				data_dir=/fs/clip-xling/projects/xformal/data/formality_classifiers_data/$test_lang
				# xlm-r and mbert were not finetuned for differnt number of epochs
				results_dir=$output_dir/$test_lang/$base_model/$learning_rate/$tune_task/
				# uncomment for facebook/mbart
				# results_dir=$output_dir/$test_lang/$base_model/$learning_rate/$tune_task/$epoch
				args=""
				inf_args=""
				suffix=""
			elif [[ $tune_task == classifier_on_regression ]]; then
				data_dir=/fs/clip-xling/projects/xformal/data/formality_regression_data/$test_lang
				# xlm-r and mbert were not finetuned for differnt number of epochs
				# results_dir=$output_dir/$test_lang/$base_model/$learning_rate/$tune_task/
				results_dir=$output_dir/$test_lang/$base_model/$learning_rate/binary_classification/
				args=""
				inf_args=" --eval_classification "
				suffix="_regression"
			else
				data_dir=/fs/clip-xling/projects/xformal/data/formality_regression_data/$test_lang
				results_dir=$output_dir/$test_lang/$base_model/$learning_rate/$tune_task/$epoch
				args=" -r "
				inf_args=" --is_regression "
				suffix=""
				echo $results_dir
			fi;
			# translate-train
			if [ ! -f $results_dir/results_translate_train_${test_lang}${suffix}.txt ]; then
				 python run_gyafc.py \
					--model_name_or_path $results_dir/ \
					--do_predict \
					--train_file $data_dir/train.csv \
					--validation_file $data_dir/tune.csv \
					--test_file $data_dir/test.csv \
					--logging_dir $run_dir \
					--per_device_eval_batch_size $batch_size \
					--cache_dir $TRANSFORMERS_CACHE \
					--output_dir $results_dir/  \
					--eval_accumulation_steps 1 \
					${inf_args}

				mv $results_dir/test_results_None.txt $results_dir/results_translate_train_${test_lang}${suffix}.txt
			fi;

			if [[ $tune_task != classifier_on_regression ]]; then
				python run_eval.py -g $data_dir/test.csv -p $results_dir/results_translate_train_${test_lang}${suffix}.txt -o $results_dir/eval_translate_train_${test_lang}${suffix}.json ${args}
			fi;

			if [ $test_lang != en ]; then 

				if [[ $tune_task == binary_classification ]]; then
					model_name_or_path=$output_dir/en/$base_model/$learning_rate/$tune_task/
				elif [[ $tune_task == classifier_on_regression ]]; then
					model_name_or_path=$output_dir/en/$base_model/$learning_rate/binary_classification/
				else
					model_name_or_path=$output_dir/en/$base_model/$learning_rate/$tune_task/$epoch/
				fi;

				# translate-test
				if [ ! -f $results_dir/results_translate_test_${test_lang}${suffix}.txt ]; then
					python run_gyafc.py \
						--model_name_or_path $model_name_or_path \
						--do_predict \
									--train_file $data_dir/train.csv \
									--validation_file $data_dir/tune.csv \
						--test_file $data_dir/translate_test.csv \
						--logging_dir $run_dir \
						--per_device_eval_batch_size $batch_size \
						--cache_dir $TRANSFORMERS_CACHE \
						--output_dir $results_dir/  \
						${inf_args}

					mv $results_dir/test_results_None.txt $results_dir/results_translate_test_${test_lang}${suffix}.txt
				fi;

				if [[ $tune_task != classifier_on_regression ]]; then
					python run_eval.py -g $data_dir/translate_test.csv -p $results_dir/results_translate_test_${test_lang}${suffix}.txt -o $results_dir/eval_translate_test_${test_lang}${suffix}.json ${args}
				fi;

				# zero-shot
				if [ ! -f $results_dir/results_zero_shot_${test_lang}${suffix}.txt ]; then
					python run_gyafc.py \
						--model_name_or_path $model_name_or_path \
						--do_predict \
									--train_file $data_dir/train.csv \
									--validation_file $data_dir/tune.csv \
						--test_file $data_dir/test.csv \
						--logging_dir $run_dir \
						--per_device_eval_batch_size $batch_size \
						--cache_dir $TRANSFORMERS_CACHE \
						--output_dir $results_dir/  \
						${inf_args}

					mv $results_dir/test_results_None.txt $results_dir/results_zero_shot_${test_lang}${suffix}.txt
				fi;
				if [[ $tune_task != classifier_on_regression ]]; then
					python run_eval.py -g $data_dir/test.csv -p $results_dir/results_zero_shot_${test_lang}${suffix}.txt -o $results_dir/eval_zero_shot_${test_lang}${suffix}.json ${args}
				fi;
			fi;
		done;
	done;
done;
