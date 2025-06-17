import pandas as pd
import re
from pipeline_task import PipelineTask
from task_reference import TaskReference

class ApplyStemming(PipelineTask):
    def __init__(self, column_name : str):
        super().__init__(TaskReference.APPLYSTEMMING, column_name)

    def do_work(self, current_data : pd.DataFrame) -> pd.DataFrame:
        return current_data