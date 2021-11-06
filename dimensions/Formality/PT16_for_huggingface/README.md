# Formality Regressors for Multilingual Formality Evaluation

This repository contains data for training a formality regressor model for English.
The training/test/dev split is random. 

The data is collected from Ellie Pavlick and Joel Tetreault in [1](https://aclanthology.org/Q16-1005/). 

Fine-tuning multilingual pre-trained models on this data is found to correlate best
with human evaluation judgments collected in [2](https://aclanthology.org/N18-1012/) and [3](https://aclanthology.org/2021.naacl-main.256/) for Formality Style Transfer in the following languages:
English, French,  Italian, and Brazilian-Portuguese [4](https://aclanthology.org/2021.emnlp-main.100/).
 
**Note:** The regressor is used in a zero-shot setting for languages other than English.

If you use the regressor model please cite the following papers

```
@article{pavlick-tetreault-2016-empirical,
    title = "An Empirical Analysis of Formality in Online Communication",
    author = "Pavlick, Ellie  and
      Tetreault, Joel",
    journal = "Transactions of the Association for Computational Linguistics",
    volume = "4",
    year = "2016",
    url = "https://aclanthology.org/Q16-1005",
    doi = "10.1162/tacl_a_00083",
    pages = "61--74",
    abstract = "This paper presents an empirical study of linguistic formality. We perform an analysis of humans{'} perceptions of formality in four different genres. These findings are used to develop a statistical model for predicting formality, which is evaluated under different feature settings and genres. We apply our model to an investigation of formality in online discussion forums, and present findings consistent with theories of formality and linguistic coordination.",
}
```

```
@inproceedings{briakou-etal-2021-ola,
    title = "Ol{\'a}, Bonjour, Salve! {XFORMAL}: A Benchmark for Multilingual Formality Style Transfer",
    author = "Briakou, Eleftheria  and
      Lu, Di  and
      Zhang, Ke  and
      Tetreault, Joel",
    booktitle = "Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jun,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.naacl-main.256",
    doi = "10.18653/v1/2021.naacl-main.256",
    pages = "3199--3216",
    abstract = "We take the first step towards multilingual style transfer by creating and releasing XFORMAL, a benchmark of multiple formal reformulations of informal text in Brazilian Portuguese, French, and Italian. Results on XFORMAL suggest that state-of-the-art style transfer approaches perform close to simple baselines, indicating that style transfer is even more challenging when moving multilingual.",
}
```

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
@inproceedings{rao-tetreault-2018-dear,
    title = "Dear Sir or Madam, May {I} Introduce the {GYAFC} Dataset: Corpus, Benchmarks and Metrics for Formality Style Transfer",
    author = "Rao, Sudha  and
      Tetreault, Joel",
    booktitle = "Proceedings of the 2018 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)",
    month = jun,
    year = "2018",
    address = "New Orleans, Louisiana",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/N18-1012",
    doi = "10.18653/v1/N18-1012",
    pages = "129--140",
    abstract = "Style transfer is the task of automatically transforming a piece of text in one particular style into another. A major barrier to progress in this field has been a lack of training and evaluation datasets, as well as benchmarks and automatic metrics. In this work, we create the largest corpus for a particular stylistic transfer (formality) and show that techniques from the machine translation community can serve as strong baselines for future work. We also discuss challenges of using automatic metrics.",
}
```
