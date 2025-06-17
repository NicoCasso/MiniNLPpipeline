import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

from pipeline_task import PipelineTask
from task_reference import TaskReference

class Tokenize(PipelineTask):
    """
    input : a str column of the dataframe 
    output : a list[str] column of the dataframe 
    """
    def __init__(self, column_name : str):
        super().__init__(TaskReference.TOKENIZE, column_name)

    def tokenize(self, text:str) -> list[str]:
        word_tokens = word_tokenize(text)
        return word_tokens

    def do_work(self, current_data : pd.DataFrame) -> pd.DataFrame:
        current_data[self.column_name] = current_data[self.column_name].apply(self.tokenize)
        return current_data