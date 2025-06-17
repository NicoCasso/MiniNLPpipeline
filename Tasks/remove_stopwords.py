import pandas as pd
import nltk
from nltk.corpus import stopwords as sw
from nltk.tokenize import word_tokenize
from pipeline_task import PipelineTask
from task_reference import TaskReference

class RemoveStopwords(PipelineTask):
    """
    input : a list[str] column of the dataframe 
    output : a list[str] column of the dataframe 
    """
    def __init__(self, column_name : str):
        super().__init__(TaskReference.REMOVESTOPWORDS, column_name)
        self.all_words : set[str] = []

    def remove_stopwords(self, word_list:list[str]) -> list[str]:
        stop_words = set(sw.words("english"))
        filtered_list = [word for word in word_list if word not in stop_words]
        return filtered_list

    def do_work(self, current_data : pd.DataFrame) -> pd.DataFrame:
        current_data[self.column_name] = current_data[self.column_name].astype(list[str]).apply(self.remove_stopwords)
        return current_data