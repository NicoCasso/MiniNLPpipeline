import pandas as pd
from pipeline_task import PipelineTask
from task_reference import TaskReference

class ConvertToLowercase(PipelineTask):
    """
    input : a str column of the dataframe 
    output : a str column of the dataframe 
    """
    def __init__(self, column_name : str):
        super().__init__(TaskReference.CONVERTTOLOWERCASE, column_name)

    def do_work(self, current_data : pd.DataFrame) -> pd.DataFrame:
        current_data[self.column_name] = current_data[self.column_name].str.lower()
        return current_data