import pandas as pd
import Tasks
import nltk
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
                case TaskReference.REMOVEHTMLTAG : 
                    current_task = Tasks.RemoveHtmlTags(column_name)
                case TaskReference.CONVERTTOLOWERCASE :
                    current_task = Tasks.ConvertToLowercase(column_name)
                case TaskReference.REMOVENUMBER : 
                    current_task = Tasks.RemoveNumber(column_name)
                case TaskReference.CONVERTNUMERICALVALUES : 
                    current_task =Tasks.ConvertToNumericalValues(column_name)
                case TaskReference.REMOVEPUNCTUATION : 
                    current_task =Tasks.RemovePunctuation(column_name)
                case TaskReference.REMOVEWHITESPACE : 
                    current_task =Tasks.RemoveWhiteSpace(column_name)
                case TaskReference.TOKENIZE : 
                    current_task =Tasks.Tokenize(column_name)
                case TaskReference.REMOVESTOPWORDS : 
                    nltk.download('stopwords')
                    current_task =Tasks.RemoveStopwords(column_name)
                case TaskReference.APPLYSTEMMING : 
                    current_task =Tasks.ApplyStemming(column_name)
                case TaskReference.APPLYLEMMATIZATION : 
                    nltk.download('wordnet')
                    current_task = Tasks.ApplyLemmatization(column_name)

            try :
                current_data = current_task.do_work(current_data)
                print(f"{str(current_task.reference)} done.")
            except Exception as ex:
                print(f"Error in {str(current_task.reference)}")

        return current_data
                    
    
    