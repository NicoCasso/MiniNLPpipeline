import pandas as pd
import re
from pipeline_task import PipelineTask
from task_reference import TaskReference
import inflect

class ConvertToNumericalValues(PipelineTask):
    def __init__(self, column_name : str):
        super().__init__(TaskReference.CONVERTNUMERICALVALUES, column_name)
        self.inflect_engine = inflect.engine()

    def convert_number(self, text: str):
        temp_str = text.split()
        new_string = []
        for word in temp_str:
            if word.isdigit():
                temp = self.inflect_engine.number_to_words(word)
                new_string.append(temp)
            else:
                new_string.append(word)

        temp_str = ' '.join(new_string)
        return temp_str
    
    def do_work(self, current_data : pd.DataFrame) -> pd.DataFrame:
        current_data[self.column_name] = current_data[self.column_name].apply(self.convert_number)
        return current_data