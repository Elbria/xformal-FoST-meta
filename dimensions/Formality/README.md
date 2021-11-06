# Formality Regressors for Multilingual Formality Evaluation

This repository describes how to obtain formality regressors for multilingual automatic evaluation of Formality Style
Transfer (FoST).

The evaluation is based on a *single* model that fine-tunes XLM-R [1](https://aclanthology.org/2020.acl-main.747.pdf)
on English formality ratings [2](https://aclanthology.org/Q16-1005/). Evaluation on languages other than
English is performed in a zero-shot setting.

The above implementation is based on [Huggingface Transformers](https://github.com/huggingface/transformers).

## Setup

    cd transformers/
    pip install -e .
    cd ..

## Training Formality Regressor

    bash train.sh

## Evaluate Formality Regressor

    bash inference_formality.sh
    

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
```
@inproceedings{conneau-etal-2020-unsupervised,
    title = "Unsupervised Cross-lingual Representation Learning at Scale",
    author = "Conneau, Alexis  and
      Khandelwal, Kartikay  and
      Goyal, Naman  and
      Chaudhary, Vishrav  and
      Wenzek, Guillaume  and
      Guzm{\'a}n, Francisco  and
      Grave, Edouard  and
      Ott, Myle  and
      Zettlemoyer, Luke  and
      Stoyanov, Veselin",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2020.acl-main.747",
    doi = "10.18653/v1/2020.acl-main.747",
    pages = "8440--8451",
    abstract = "This paper shows that pretraining multilingual language models at scale leads to significant performance gains for a wide range of cross-lingual transfer tasks. We train a Transformer-based masked language model on one hundred languages, using more than two terabytes of filtered CommonCrawl data. Our model, dubbed XLM-R, significantly outperforms multilingual BERT (mBERT) on a variety of cross-lingual benchmarks, including +14.6{\%} average accuracy on XNLI, +13{\%} average F1 score on MLQA, and +2.4{\%} F1 score on NER. XLM-R performs particularly well on low-resource languages, improving 15.7{\%} in XNLI accuracy for Swahili and 11.4{\%} for Urdu over previous XLM models. We also present a detailed empirical analysis of the key factors that are required to achieve these gains, including the trade-offs between (1) positive transfer and capacity dilution and (2) the performance of high and low resource languages at scale. Finally, we show, for the first time, the possibility of multilingual modeling without sacrificing per-language performance; XLM-R is very competitive with strong monolingual models on the GLUE and XNLI benchmarks. We will make our code and models publicly available.",
}
```
```
@inproceedings{wolf-etal-2020-transformers,
    title = "Transformers: State-of-the-Art Natural Language Processing",
    author = "Thomas Wolf and Lysandre Debut and Victor Sanh and Julien Chaumond and Clement Delangue and Anthony Moi and Pierric Cistac and Tim Rault and Rémi Louf and Morgan Funtowicz and Joe Davison and Sam Shleifer and Patrick von Platen and Clara Ma and Yacine Jernite and Julien Plu and Canwen Xu and Teven Le Scao and Sylvain Gugger and Mariama Drame and Quentin Lhoest and Alexander M. Rush",
    booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
    month = oct,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.emnlp-demos.6",
    pages = "38--45"
}
```