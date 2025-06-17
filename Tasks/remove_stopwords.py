import pandas as pd
import nltk
from nltk.corpus import stopwords as sw
from nltk.tokenize import word_tokenize
from pipeline_task import PipelineTask
from task_reference import TaskReference

class RemoveStopwords(PipelineTask):
    def __init__(self, column_name : str):
        super().__init__(TaskReference.REMOVESTOPWORDS, column_name)
        self.all_words : set[str] = []

    def remove_stopwords(self, text:str):
        stop_words = set(sw.words("english"))
        word_tokens = word_tokenize(text)
        filtered_text = [word for word in word_tokens if word not in stop_words]
        return filtered_text

    def do_work(self, current_data : pd.DataFrame) -> pd.DataFrame:
        current_data[self.column_name] = current_data[self.column_name].apply(self.remove_stopwords)
        return current_data