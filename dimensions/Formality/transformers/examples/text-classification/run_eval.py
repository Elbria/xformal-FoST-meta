import argparse
import csv
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix
import pandas as pd
from scipy.stats import pearsonr, spearmanr
import json

def read_file(gold_file,  pred_file):
	metric_scores = pd.read_csv(pred_file, sep="\t")["prediction"].values
	human_scores = pd.read_csv(gold_file, sep=",")["label"].values

	indices = [i for i in range(len(human_scores)) if human_scores[i]!='None']
	metric_scores = [metric_scores[i] for i in indices]
	human_scores = [float(human_scores[i]) for i in indices]
	
	return metric_scores, human_scores


def compute_accuracy(gold_file,  pred_file):
	y_pred, y_true = read_file(gold_file,  pred_file)
	micro_p, micro_r, micro_f1, _ = precision_recall_fscore_support(y_true, y_pred, average='micro')
	macro_p, macro_r, macro_f1, _ = precision_recall_fscore_support(y_true, y_pred, average='macro')

	results = {
		"Accuracy": accuracy_score(y_true, y_pred),
		"MicroPrecision": micro_p,
		"MicroRecall": micro_r,
		"MicroF1": micro_f1,
		"MacroPrecision": macro_p,
		"MacroRecall": macro_r,
		"MacroF1": macro_f1,
	}
	return results


def compute_correlation(gold_file,  pred_file):
	y_pred, y_true = read_file(gold_file,  pred_file)
	results = {
			"Pearson":  pearsonr(y_true, y_pred),
			"Spearman": spearmanr(y_true, y_pred)
	}
	return results

def main():
	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument("-g", "--gold-file", required=True, help="gold labels")
	arg_parser.add_argument("-p", "--pred-file", required=True, help="model predictions")
	arg_parser.add_argument("-o", "--output-file", required=True, help="model predictions")
	arg_parser.add_argument("-r", '--regression', action='store_true', help="regression task")
	args = arg_parser.parse_args()

	if args.regression:
		results = compute_correlation(args.gold_file, args.pred_file)
	else:
		results = compute_accuracy(args.gold_file, args.pred_file)

	with open(args.output_file, 'w') as fp:
	    json.dump(results, fp)

if __name__ == '__main__':
	main()