# Evaluating the Evaluation Metrics for Style Transfer: A Case Study in Multilingual Formality Transfer

This repository contains code and data from the EMNLP 2021 paper that can be found [here](https://aclanthology.org/2021.emnlp-main.100/)!

We outline best practices for automatic evaluation in (formality) style transfer and identify several models that correlate well with human judgments and are robust across languages.
We hope that this work will help accelerate development in ST, where human evaluation is often challenging to collect.

## Outline

* **best-practices**: contains code for best performing automatic evaluation metrics for FoST for 3 dimensions: formality, meaning, and fluency.
* **meta-evaluation-files**: contains system outputs rated by humans and several automatic metrics for 3 evaluation dimensions (i.e., formality, meaning, and fluency) and 4 languages (i.e., English,
French, Italian, and Brazilian-Portuguese).
* **scripts**: contains scripts for running other metrics (beyond the best performing ones) covered in our study.

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