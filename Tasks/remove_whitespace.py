import pandas as pd
from pipeline_task import PipelineTask
from task_reference import TaskReference

class RemoveWhiteSpace(PipelineTask):
    def __init__(self, column_name : str):
        super().__init__(TaskReference.REMOVEWHITESPACE, column_name)

    def remove_whitespace(self, text:str):
        return  " ".join(text.split())

    def do_work(self, current_data : pd.DataFrame) -> pd.DataFrame:
        return current_data