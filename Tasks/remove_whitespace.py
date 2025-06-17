import pandas as pd
import re
from pipeline_task import PipelineTask
from task_reference import TaskReference

class RemoveWhiteSpace(PipelineTask):
    def __init__(self, column_name : str):
        super().__init__(TaskReference.REMOVEWHITESPACE, column_name)

    def do_work(self, current_data : pd.DataFrame) -> pd.DataFrame:
        return current_data