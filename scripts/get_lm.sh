#!/bin/bash
# Sweta Agrawal
set -e

# get the parent directory of this script.
export LC_CTYPE=en_US.UTF-8
export LC_ALL=en_US.UTF-8

# add path to the bin folder, eg kenlm/build/bin
kenlm_path=kenlm/build/bin

# download OpenSubs
src=en
lang=$1
name=OpenSubtitles
version=v2016
global_data_dir=data/$src-$lang

if [ ! -d $global_data_dir ]; then
	mkdir -p $global_data_dir
	cd $global_data_dir
	wget -O $src-$lang.txt.zip http://opus.nlpl.eu/download.php?f=${name}/${version}/moses/$src-$lang.txt.zip 
	unzip $src-$lang.txt.zip 
	rm $src-$lang.txt.zip 
	cd ../../
fi;

lm_dir=language_models/$lang
lm_data_dir=data/$src-$lang
mkdir -p $lm_dir
lm=$lm_dir/$name.lm

# Training language models
if [ ! -f $lm.bin ]; then
	echo " * Training LM for ${corpus} ..."
	cat $lm_data_dir/$name.$src-$lang.$lang \
		| $kenlm_path/lmplz --order 5 -S 30G -T $lm_dir/ \
		> $lm
    $kenlm_path/build_binary $lm $lm.bin
	rm $lm
fi;

if [ $lang == fr ]; then
	# For english
	lm_dir=language_models/en
	lm_data_dir=data/$src-$lang
	lm=$lm_dir/$name.lm

	# Training language models
	if [ ! -f $lm.bin ]; then
		echo " * Training LM for ${corpus} ..."
		cat $lm_data_dir/$name.$src-$lang.en \
			| $kenlm_path/lmplz --order 5 -S 30G -T $lm_dir/ \
			> $lm
	    $kenlm_path/build_binary $lm $lm.bin
		rm $lm
	fi;
fi;