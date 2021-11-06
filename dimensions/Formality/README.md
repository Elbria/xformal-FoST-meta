# Formality Regressors for Multilingual Formality Evaluation

This repository describes how to obtain formality regressors for multilingual automatic evaluation of Formality Style
Transfer (FoST), as detailed in [Evaluating the Evaluation Metrics for Style Transfer: A Case Study in Multilingual Formality Transfer](https://aclanthology.org/2021.emnlp-main.100/).

The evaluation is based on a *single* model that fine-tunes XLM-R [1](https://aclanthology.org/2020.acl-main.747.pdf)
on English formality ratings [2](https://aclanthology.org/Q16-1005/). Evaluation on languages other than
English is performed in a zero-shot setting.


## Requirements
This repo is based on [Huggingface Transformers](https://github.com/huggingface/transformers). Please
follow the instructions in the above repo for requirements and install transformers from source locally with:

    cd transformers/
    pip install -e .
    cd ..

## Training Formality Regressor
To train a formality regressor from scratch on data provided unsed PT16_for_huggingface execute the command
below:

    bash train.sh

## Evaluate Formality Regressor
Evaluate the regressor using the below script (you may need to adjust path in the evaluation script):

    bash inference_formality.sh

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
