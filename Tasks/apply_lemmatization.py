import pandas as pd

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

from pipeline_task import PipelineTask
from task_reference import TaskReference

class ApplyLemmatization(PipelineTask):
    def __init__(self, column_name : str):
        super().__init__(TaskReference.APPLYLEMMATIZATION, column_name)
        self.lemmatizer = WordNetLemmatizer()

    def lemma_words(self, text:str):
        word_tokens = word_tokenize(text)
        lemmas = [self.lemmatizer.lemmatize(word) for word in word_tokens]
        return lemmas

    def do_work(self, current_data : pd.DataFrame) -> pd.DataFrame:
        current_data[self.column_name] = current_data[self.column_name].apply(self.lemma_words)
        return current_data