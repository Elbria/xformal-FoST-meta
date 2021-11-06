# Multilingual Formality Evaluation: Meaning Evaluation aspect

For automatic evaluation of meaning preservation between an informal text (system input) and a formal text (system output)
we suggest using the chrF score of Maja Popović (detailed description is found in the
[chrF: character n-gram F-score for automatic MT evaluation](https://aclanthology.org/W15-3049/);
official implementation is [here](https://github.com/m-popovic/chrF)).


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
@inproceedings{popovic-2015-chrf,
    title = "chr{F}: character n-gram {F}-score for automatic {MT} evaluation",
    author = "Popovi{\'c}, Maja",
    booktitle = "Proceedings of the Tenth Workshop on Statistical Machine Translation",
    month = sep,
    year = "2015",
    address = "Lisbon, Portugal",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/W15-3049",
    doi = "10.18653/v1/W15-3049",
    pages = "392--395",
}
```
