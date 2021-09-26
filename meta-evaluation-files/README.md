# Description

The meta-files of this repository contain human ratings and automatic evaluation scores
for Formality Style Transfer systems in four languages: English (EN), Brazilian Portuguese (BR-PT), Italian (IT),
and French (FR).

The human ratings are collected by [Rao & Tetreault](https://aclanthology.org/N18-1012/) for EN and
and by [Briakou et al](https://aclanthology.org/2021.naacl-main.256/) for BR-PT, IT, and FR.
Details on the automatic evaluation metrics are described in our paper: [Evaluating the Evaluation Metrics for Style Transfer: A Case Study in Multilingual Formality Transfer]().

# Obtaining Meta-evaluation Files

The extracted meta-evaluation files are created based on XFORMAL and GYAFC evaluation datasets.
To obtain access to them, follow the instructions under [Obtaining XFORMAL](https://github.com/Elbria/xformal-FoST).

A short description of the content of the meta-files used in our study is given below:

| Name | Description |
| --- | --- |
| `system_name` |   Name of system |
| `informal_input` | Informal input  |
| `system_output` | Formal rewrite of informal input for given system    |
| `meaning_human` | Human rating of meaning similarity between the informal input and the formal system output   |
| `formality_human` |  Human rating of formality for a given system output   |
| `fluency_human` |  Human rating of fluency for a given system output   |
| `combined` | Overall human rating between the informal input and the formal system output  |
| `self-cosine` | Cosine distance between embeddings of informal input and formal system output |
| `self-wmd` | Word's Movers Distance between embeddings of informal input and formal system output |
| `ref-cosine` | Cosine distance between embeddings of formal reference and formal system output |
| `ref-wmd` | Word's Movers Distance between embeddings of formal reference and formal system output |
| `ref-BLEU` | BLEU score between formal reference and formal system output |
| `self-BLEU` |  BLEU score between informal input and formal system output |
| `ref-Chrf` | chrF score between formal reference and formal system output |
| `self-Chrf` | chrF score between informal input and formal system output |
| `ref-Meteor` | METEOR score between formal reference and formal system output |
| `self-Meteor` | METEOR score between input and formal system output |
| `ref-BERTScore` | BERT-Score between formal reference and formal system output |
| `self-BERTScore` | BERT-Score between informal input and formal system output |
| `ref STS Bert (T-Train)` | Similarity of formal reference/system output for mBERT model fine-tuned on STS with Translate-Train |
| `self STS Bert (T-Train)` | Similarity of formal reference/system output  for mBERT model fine-tuned on STS with Translate-Train |
| `ref STS Bert  (Zero-Shot)` | Similarity of formal reference/system output  for mBERT model fine-tuned on STS with Zero-Shot |
| `self STS Bert (Zero-Shot)` | Similarity of formal reference/system output  for mBERT model fine-tuned on STS with Zero-Shot |
| `ref STS XLM (T-Train)` | Similarity of formal reference/system output  for XLM-R model fine-tuned on STS with Translate-Train |
| `self STS XLMR (T-Train)` | Similarity of formal reference/system output  for XLM-R model fine-tuned on STS with Translate-Train |
| `ref STS XLM (Zero-Shot)` | Similarity of formal reference/system output  for XLM-R model fine-tuned on STS with Zero-Shot |
| `self STS XLMR (Zero-Shot)` | Similarity of formal reference/system output  for XLM-R model fine-tuned on STS with Zero-Shot |
| `XLM-R (T-Train)` | Formality score of system output for XLM-R model fine-tuned on PT16 with Translate-Train |
| `XLM-R (ZT)` | Formality score of system output for XLM-R model fine-tuned on PT16 with Zero-Shot |
| `XLM-R (T-Test)` | Formality score of system output for XLM-R model fine-tuned on PT16 with Translate-Test |
| `mBERT (T-Train)` | Formality score of system output for mBERT model fine-tuned on PT16 with Translate-Train |
| `mBERT (ZT)` | Formality score of system output for mBERT model fine-tuned on PT16 with Zero-Shot |
| `mBERT (T-Test)` | Formality score of system output for mBERT model fine-tuned on PT16 with Translate-Test |
| `pseudo-ppl-xlm` | Pseudo-perplexity score of system output from XLM-R |
| `pseudo-ppl-mbert` | Pseudo-perplexity score of system output from mBERT |
| `likelihood` | Likelihood of KenLM models for system output |
| `perplexity` | Perplexity of KenLM models for system output |

