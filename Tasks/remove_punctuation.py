import pandas as pd
import string
from pipeline_task import PipelineTask
from task_reference import TaskReference

class RemovePunctuation(PipelineTask):
    """
    input : a str column of the dataframe 
    output : a str column of the dataframe 
    """
    def __init__(self, column_name : str):
        super().__init__(TaskReference.REMOVEPUNCTUATION, column_name)

    def remove_punctuation(self, text:str) ->str:
        translator = str.maketrans('', '', string.punctuation)
        return text.translate(translator)

    def do_work(self, current_data : pd.DataFrame) -> pd.DataFrame:
        return current_data