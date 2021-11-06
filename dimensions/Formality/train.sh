#!/bin/bash

# Fine-tune XLM-R on Eglish formality ratings

export TRANSFORMERS_CACHE=outputs/cache
output_dir=outputs/model
run_dir=outputs/run

base_models="xlm-roberta-base"
learning_rates="5e-5"
epochs="5"
tune_task=regression
data_dir=PT16_for_huggingface/
train_script=transformers/examples/text-classification/run_gyafc.py

python $train_script \
        --model_name_or_path $base_model \
        --do_train \
        --do_eval \
       	--train_file $data_dir/train.csv \
        --validation_file $data_dir/tune.csv \
        --max_seq_length 128 \
        --per_device_train_batch_size 32 \
        --learning_rate $learning_rate \
        --num_train_epochs $epoch \
      	--logging_dir $run_dir \
       	--cache_dir $TRANSFORMERS_CACHE \
        --output_dir $output_dir \
