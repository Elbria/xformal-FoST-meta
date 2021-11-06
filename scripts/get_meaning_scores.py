# Sweta Agrawal

import pandas as pd
from scipy.stats import pearsonr, spearmanr
import sys
import metrics
import argparse

def get_scores(input_file, metric_name, lang, ref=False):
	data = pd.read_csv(input_file, "\t")
	# print(data.columns)

	if metric_name=="BERTScoreMetric":
		# to ensure that multilingual model is loaded for all lang
		# https://github.com/Tiiiger/bert_score/blob/master/bert_score/utils.py#L29
		lang="fr"

	metric = getattr(metrics, metric_name)(lang)
	references = list(zip(data["rewrite0"].to_list(), data["rewrite1"].to_list(), data["rewrite2"].to_list(), data["rewrite3"].to_list()))

	if ref:
		references = list(zip(data["rewrite0"].to_list(), data["rewrite1"].to_list(), data["rewrite2"].to_list(), data["rewrite3"].to_list()))
	else:
		references = list(zip(data["system_input"].to_list()))

	outputs = data["segment"].to_list()
	metric_scores = metric.get_score(references, outputs)
	human_scores = list(map(float, data["Aggregated_score"].to_list()))

	assert len(metric_scores) == len(human_scores)
	print("%s (Ref=%d) Pearson(%s): %.3f" %(metric_name, int(ref), lang, pearsonr(metric_scores, human_scores)[0]))
	print("%s (Ref=%d) Spearman(%s): %.3f" %(metric_name, int(ref), lang, spearmanr(metric_scores, human_scores)[0]))
	return metric_scores

def write_scores(metric_scores, fname):
	with open(fname, 'w') as f:
		f.write("ref-BLEU\tself-BLEU\tref-Chrf\tself-Chrf\tref-Meteor\tself-Meteor\tref-BERTScore\tself-BERTScore\n")
		for scores in metric_scores:
			f.write(("\t").join(list(map(str, scores))) + "\n")

def main():

	arg_parser = argparse.ArgumentParser(description='Extract LM scores from trained kenlm model')
	arg_parser.add_argument('--results_file', '-s', type=str, default=None)
	arg_parser.add_argument('--input_file', '-s', type=str, default=None)
	arg_parser.add_argument('--lang', '-s', type=str, default=None)
	
	metric_names = ["BERTScoreMetric", "BleuMetric", "ChrfMetric", "MeteorMetric" ]

	all_metric_scores = []
	for metric_name in metric_names:
		ref_metric_scores = get_scores(args.input_file, args.metric_name, args.lang, ref=True)
		all_metric_scores.append(ref_metric_scores)
		self_metric_scores = get_scores(args.input_file, args.metric_name, args.lang)
		all_metric_scores.append(self_metric_scores)
	all_metric_scores = list(zip(*all_metric_scores))
	write_scores(all_metric_scores, args.results_file)
		

if __name__ == '__main__':
	main() 