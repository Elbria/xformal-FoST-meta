# Multilingual Formality Evaluation: Fluency aspect

For automatic evaluation of fluency of a formal text (system output)
we suggest using pseudo-perplexity scores as described in [Salazar et al](https://aclanthology.org/2020.acl-main.240/)
based on XLM-R [[1]](https://aclanthology.org/2020.acl-main.747.pdf).

**Note:** Pseudo-perplexity scores are found to correlate moderately with human judgments! Please draw conclusions
accordingly :)

## Contact
If you use any contents of this repository, please cite us. For any questions, write to ebriakou@cs.umd.edu.

```
@inproceedings{briakou-etal-2021-evaluating,
    title = "Evaluating the Evaluation Metrics for Style Transfer: A Case Study in Multilingual Formality Transfer",
    author = "Briakou, Eleftheria  and
      Agrawal, Sweta  and
      Tetreault, Joel  and
      Carpuat, Marine",
    booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2021",
    address = "Online and Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.emnlp-main.100",
    pages = "1321--1336",
    abstract = "While the field of style transfer (ST) has been growing rapidly, it has been hampered by a lack of standardized practices for automatic evaluation. In this paper, we evaluate leading automatic metrics on the oft-researched task of formality style transfer. Unlike previous evaluations, which focus solely on English, we expand our focus to Brazilian-Portuguese, French, and Italian, making this work the first multilingual evaluation of metrics in ST. We outline best practices for automatic evaluation in (formality) style transfer and identify several models that correlate well with human judgments and are robust across languages. We hope that this work will help accelerate development in ST, where human evaluation is often challenging to collect.",
}
```

```
@inproceedings{salazar-etal-2020-masked,
    title = "Masked Language Model Scoring",
    author = "Salazar, Julian  and
      Liang, Davis  and
      Nguyen, Toan Q.  and
      Kirchhoff, Katrin",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.acl-main.240",
    doi = "10.18653/v1/2020.acl-main.240",
    pages = "2699--2712",
    abstract = "Pretrained masked language models (MLMs) require finetuning for most NLP tasks. Instead, we evaluate MLMs out of the box via their pseudo-log-likelihood scores (PLLs), which are computed by masking tokens one by one. We show that PLLs outperform scores from autoregressive language models like GPT-2 in a variety of tasks. By rescoring ASR and NMT hypotheses, RoBERTa reduces an end-to-end LibriSpeech model{'}s WER by 30{\%} relative and adds up to +1.7 BLEU on state-of-the-art baselines for low-resource translation pairs, with further gains from domain adaptation. We attribute this success to PLL{'}s unsupervised expression of linguistic acceptability without a left-to-right bias, greatly improving on scores from GPT-2 (+10 points on island effects, NPI licensing in BLiMP). One can finetune MLMs to give scores without masking, enabling computation in a single inference pass. In all, PLLs and their associated pseudo-perplexities (PPPLs) enable plug-and-play use of the growing number of pretrained MLMs; e.g., we use a single cross-lingual model to rescore translations in multiple languages. We release our library for language model scoring at https://github.com/awslabs/mlm-scoring.",
}
```
