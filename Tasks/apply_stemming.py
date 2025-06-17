import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

from pipeline_task import PipelineTask
from task_reference import TaskReference

class ApplyStemming(PipelineTask):
    def __init__(self, column_name : str):
        super().__init__(TaskReference.APPLYSTEMMING, column_name)
        self.stemmer = PorterStemmer()

    def stem_words(self, text:str):
        word_tokens = word_tokenize(text)
        stems = [self.stemmer.stem(word) for word in word_tokens]
        return stems

    def do_work(self, current_data : pd.DataFrame) -> pd.DataFrame:
        current_data[self.column_name] = current_data[self.column_name].apply(self.stem_words)
        return current_data