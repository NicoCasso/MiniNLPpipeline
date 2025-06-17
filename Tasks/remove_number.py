import pandas as pd
import re
from pipeline_task import PipelineTask
from task_reference import TaskReference

class RemoveNumber(PipelineTask):
    def __init__(self, column_name : str):
        super().__init__(TaskReference.REMOVENUMBER, column_name)

    def remove_numbers(self, text):
        result = re.sub(r'\d+', '', text)
        return result

    def do_work(self, current_data : pd.DataFrame) -> pd.DataFrame:
        current_data[self.column_name] = current_data[self.column_name].apply(self.remove_numbers)
        return current_data