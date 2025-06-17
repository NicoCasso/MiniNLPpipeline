import pandas as pd

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

from pipeline_task import PipelineTask
from task_reference import TaskReference

class ApplyLemmatization(PipelineTask):
    """
    input : a list[str] column of the dataframe 
    output : a list[str] column of the dataframe 
    """
    def __init__(self, column_name : str):
        super().__init__(TaskReference.APPLYLEMMATIZATION, column_name)
        self.lemmatizer = WordNetLemmatizer()

    def lemma_words(self, text_list:list[str]) -> list[str]:
        lemmas = [self.lemmatizer.lemmatize(word) for word in text_list]
        return lemmas

    def do_work(self, current_data : pd.DataFrame) -> pd.DataFrame:
        current_data[self.column_name] = current_data[self.column_name].apply(
            self.safe_cast_to_str_list).apply(self.lemma_words)
        return current_data