import pandas as pd
import re
import Tasks.convert_numerical_values
import Tasks.convert_to_lowercase
import Tasks.remove_html_tags
import Tasks.remove_number
import Tasks.remove_punctuation
from task_reference import TaskReference
from pipeline_task import PipelineTask
import Tasks

class CustomPipeline():
    def __init__(self):
        self.tasks : list[TaskReference]= [] 

    def do_work(self, data : pd.DataFrame, column_name:str) -> pd.DataFrame :
        current_data = data.copy()
        for task_reference in self.tasks :
            
            current_task : PipelineTask = None

            match task_reference :
                case TaskReference.REMOVEHTMLTAG : current_task = Tasks.RemoveHtmlTags(column_name)
                case TaskReference.CONVERTTOLOWERCASE :current_task = Tasks.ConvertToLowercase(column_name)
                case TaskReference.REMOVENUMBER : current_task = Tasks.RemoveNumber(column_name)
                case TaskReference.CONVERTNUMERICALVALUES : Tasks.ConvertToNumericalValues(column_name)
                case TaskReference.REMOVEPUNCTUATION : Tasks.RemovePunctuation(column_name)
                case TaskReference.REMOVEWHITESPACE : Tasks.RemoveWhiteSpace(column_name)
                case TaskReference.REMOVESTOPWORDS : Tasks.RemoveStopwords(column_name)
                case TaskReference.APPLYSTEMMING : Tasks.ApplyStemming(column_name)
                case TaskReference.APPLYLEMMATIZATION : Tasks.ApplyLemmatization(column_name)

            try :
                current_data = current_task.do_work(current_data)
            except Exception as ex:
                print(f"Error in {str(current_task.reference)}")
                    

        return current_data
                    
    
    