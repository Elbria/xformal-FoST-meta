# Sweta Agrawal

import kenlm
from scipy.stats import pearsonr, spearmanr
import pandas as pd
import math
import argparse

ln10 = math.log(10)


def lm_scores(lm, text, ppl=False):
	lm_score = lm.score(text)
	if ppl:
		lm_score = lm.perplexity(text)
	return lm_score


def write_scores(metric_scores, fname):
	with open(fname, 'w') as f:
		f.write("likelihood\tppl\n")
		for scores in metric_scores:
			f.write(("\t").join(list(map(str, scores))) + "\n")

def get_scores(input_file, lang, ppl=False):
	data = pd.read_csv(input_file, sep="\t")
	outputs = data["segment"].to_list()
	lm = kenlm.Model("language_models/%s/OpenSubtitles.lm.bin"%(lang))
	metric_scores = [lm_scores(lm, text, ppl) for text in data["segment"].to_list()]
	human_scores = data["Aggregated_score"].to_list()
	assert len(metric_scores) == len(human_scores)
	return metric_scores

def main():

	arg_parser = argparse.ArgumentParser(description='Extract LM scores from trained kenlm model')
	arg_parser.add_argument('--results_file', '-s', type=str, default=None)
	arg_parser.add_argument('--input_file', '-s', type=str, default=None)
	arg_parser.add_argument('--lang', '-s', type=str, default=None)

	args = arg_parser.parse_args()

	scores = [get_scores(args.input_file, args.lang), get_scores(args.input_file, args.lang, True)]
	write_scores(list(zip(*scores)), args.results_file)

if __name__ == '__main__':
	main()