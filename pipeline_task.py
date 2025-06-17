import pandas as pd
from task_reference import TaskReference

class PipelineTask():
    def __init__(self, task_reference : TaskReference, column_name:str):
        self.reference = task_reference
        self.column_name = column_name

    def do_work(self, data : pd.DataFrame) -> pd.DataFrame:
        return data