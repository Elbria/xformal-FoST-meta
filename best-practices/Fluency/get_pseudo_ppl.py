# Sweta Agrawal

import sys
sys.path.append("mlm-scoring/src")
from mlm.scorers import MLMScorer, MLMScorerPT, LMScorer
from mlm.models import get_pretrained
import mxnet as mx
ctxs = [mx.cpu()] 
import argparse
import pandas as pd
from scipy.stats import pearsonr, spearmanr

def get_score(scorer, segments):
  return scorer.score_sentences(segments)

def write_scores(metric_scores, fname):
	with open(fname, 'w') as f:
		f.write("pseudo-ppl-xlm\tpseudo-ppl-mbert\n")
		for scores in metric_scores:
			f.write(("\t").join(list(map(str, scores))) + "\n")

def get_scores(input_file, model_name, lang):
	data = pd.read_csv(input_file, sep="\t")
	model, vocab, tokenizer = get_pretrained(ctxs, model_name)
	scorer = MLMScorerPT(model, vocab, tokenizer, ctxs)

	sentences = data["segment"].to_list()
	metric_scores = get_score(scorer, sentences)
	human_scores = data["Aggregated_score"].to_list()
	assert len(metric_scores) == len(human_scores)

	indices = [i for i in range(len(human_scores)) if human_scores[i]!='None']
	metric_scores = [metric_scores[i] for i in indices]
	human_scores = [float(human_scores[i]) for i in indices]
	print("Pearson(%s): %.3f" %(lang, pearsonr(metric_scores, human_scores)[0]))
	print("Spearman(%s): %.3f" %(lang, spearmanr(metric_scores, human_scores)[0]))
	return metric_scores


def main():

	arg_parser = argparse.ArgumentParser(description='Extract Pseudo ppl scores from pre-trained model')
	arg_parser.add_argument('--results_file', '-s', type=str, default=None)
	arg_parser.add_argument('--input_file', '-s', type=str, default=None)
	arg_parser.add_argument('--lang', '-s', type=str, default=None)
	scores = []
	for model_name in ["xlm-roberta-base", "bert-base-multilingual-cased"]:
		scores.append(get_scores(args.input_file, args.model_name, args.lang))	
	write_scores( list(zip(*scores)), args.results_file)

if __name__ == '__main__':
	main()