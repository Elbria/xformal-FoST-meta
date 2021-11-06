#!/bin/bash

# Evaluation of formality based on XLM-R

export TRANSFORMERS_CACHE=outputs/cache
output_dir=outputs/models
run_dir=outputs/runs

eval_script=transformers/examples/text-classification
base_model=xlm-roberta-base
learning_rate="5e-5"
tune_task=regression
batch_size=8
epoch=5

data_dir=PT16_for_huggingface
eval_dir=PT16_for_huggingface
args=" -r "
inf_args=" --is_regression "
suffix=""
model_name_or_path=$output_dir

python $eval_script/run_gyafc.py \
	--model_name_or_path $model_name_or_path \
	--do_predict \
	--train_file $data_dir/train.csv \
	--validation_file $data_dir/tune.csv \
	--test_file $data_dir/test.csv \
	--logging_dir $run_dir \
	--per_device_eval_batch_size $batch_size \
	--cache_dir $TRANSFORMERS_CACHE \
	--output_dir $output_dir/  \
	${inf_args}

