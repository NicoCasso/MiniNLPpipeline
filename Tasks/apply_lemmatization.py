import pandas as pd
import re
from pipeline_task import PipelineTask
from task_reference import TaskReference

class ApplyLemmatization(PipelineTask):
    def __init__(self, column_name : str):
        super().__init__(TaskReference.APPLYLEMMATIZATION, column_name)

    def do_work(self, current_data : pd.DataFrame) -> pd.DataFrame:
        return current_data