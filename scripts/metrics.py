# Sweta Agrawal

from bert_score import score
import sacrebleu
from nltk.translate.meteor_score import meteor_score as meteor 
import  sys
import nltk

# Automatic Metrics inherit from this class
class Metric():
  def __init__(self, lang):
    self.name = ""
    self.lang = lang

  def _get_score(self, references, outputs):
    """Add scoring method here"""
    pass

  def get_score(self, references, outputs):
    """
    Args:
      reference: list of reference translations
      output: list of system outputs
    Returns:
      first value: corpus level score
      second value: list of sentence level scores
    """
    return self._get_score(references, outputs)

class BleuMetric(Metric):
  def __init__(self, lang):
    super().__init__(lang)
    self.name = "BLEU"

  def _get_score(self, references, outputs):
    return  [sacrebleu.sentence_bleu(x, y).score for x, y in zip(outputs, references)]

class MeteorMetric(Metric):
  def __init__(self, lang):
    super().__init__(lang)
    self.name = "Meteor"

  def _get_score(self, references, outputs):
    return  [round(meteor(y, x), 4) for x, y in zip(outputs, references)]

class ChrfMetric(Metric):
  def __init__(self, lang):
    super().__init__(lang)
    self.name = "CHRF"

  def _get_score(self, references, outputs):
    return [sacrebleu.sentence_chrf(x, y).score for x, y in zip(outputs, references)]

class BERTScoreMetric(Metric):
  def __init__(self, lang):
    super().__init__(lang)
    self.name = "BERTScore"

  def _get_score(self, references, outputs):
    P, R, F1 = score(outputs, references, lang=self.lang, verbose=True)
    return F1.data.numpy()