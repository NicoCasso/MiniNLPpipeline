import pandas as pd
import re
from pipeline_task import PipelineTask

class CustomPipeline():
    def __init__(self):
        self.tasks : list[PipelineTask]= [] 

    def do_work(self, data : pd.DataFrame, column_name:str) -> pd.DataFrame :
        current_data = data.copy()
        for task in self.tasks :
            match task :
                case PipelineTask.REMOVEHTMLTAG :
                    current_data = self.do_remove_html_tags_task(current_data, column_name)

                case PipelineTask.CONVERTTOLOWERCASE :
                    current_data = self.do_remove_html_tags_task(current_data, column_name)

                case PipelineTask.REMOVENUMBER :
                    current_data = self.do_remove_number_task(current_data, column_name)

                case PipelineTask.CONVERTNUMERICALVALUES :
                    current_data = self.do_convert_numerical_values_task(current_data, column_name)

                case PipelineTask.REMOVEPUNCTUATION :
                    current_data = self.do_remove_punctuation_task(current_data, column_name)

                case PipelineTask.REMOVEWHITESPACE :
                    current_data = self.do_remove_punctuation_task(current_data, column_name)

                case PipelineTask.REMOVESTOPWORDS :
                    current_data = self.do_remove_punctuation_task(current_data, column_name)
                
                case PipelineTask.APPLYSTEMMING :
                    current_data = self.do_apply_steeming_task(current_data, column_name)

                case PipelineTask.APPLYLEMMATIZATION :
                    current_data = self.do_apply_lemmatization_task(current_data, column_name)
                    

        return current_data
                    
    # region html tags
    def do_remove_html_tags_task(self, current_data : pd.DataFrame, column_name: str) -> pd.DataFrame:
        current_data = self.remove_html_tags(current_data, "review")
        detected_tags = self.detect_all_html_tags(current_data, "review")
        for additionnal in detected_tags :
            specific_string = f"<{additionnal}"
            current_data = self.remove_specific(current_data, "review", specific_string)

        return current_data

    def detect_all_html_tags(self, data : pd.DataFrame, column_name: str) -> set[str]:
        all_tags :set[str] = set()
        for content in data[column_name].dropna():
            tag_list = self.detect_html_tags(str(content))
            all_tags.update(tag_list)

        return all_tags

    def detect_html_tags(self, text : str) -> set[str]:
        balises = re.findall(r'</?(\w+)', text)
        return set(balises)
    
    def remove_html_tags_from_line(self, line:str )->str :
        return re.sub(r'<[^>]+>', '', line)
    
    def remove_html_tags(self, data : pd.DataFrame, column_name: str) -> pd.DataFrame:
        data2 = data.copy()
        data2[column_name] = data2[column_name].apply(self.remove_html_tags_from_line)
        return data2

    def remove_specific(self, data : pd.DataFrame, column_name: str, string_to_remove) -> pd.DataFrame:
        data2 = data.copy()
        data2[column_name] = data2[column_name].str.replace(string_to_remove, '', regex=False)
        return data2
    # endregion

    # region lowercase
    def do_convert_to_lowercase_task(self, current_data: pd.DataFrame, column_name) -> pd.DataFrame :
        current_data[column_name] = current_data[column_name].str.lower()
        return current_data
    #endregion

    # region number
    def remove_numbers(self, text):
        result = re.sub(r'\d+', '', text)
        return result

    def do_remove_number_task(self, current_data: pd.DataFrame, column_name) -> pd.DataFrame :
        current_data[column_name] = current_data[column_name].apply(self.remove_numbers)
        return current_data
    #endregion

    # region numerical values
    def do_convert_numerical_values_task(self, current_data: pd.DataFrame, column_name) -> pd.DataFrame :
        return current_data
    #endregion

    # region punctuation
    def do_remove_punctuation_task(self, current_data: pd.DataFrame, column_name) -> pd.DataFrame :
        return current_data
    #endregion

    # region whitespace
    def do_remove_whitespace_task(self, current_data: pd.DataFrame, column_name) -> pd.DataFrame :
        return current_data
    #endregion

    # region stopwords
    def do_remove_stopwords_task(self, current_data: pd.DataFrame, column_name) -> pd.DataFrame :
        return current_data
    #endregion

    # region stemming
    def do_apply_stemming_task(self, current_data: pd.DataFrame, column_name) -> pd.DataFrame :
        return current_data
    #endregion

    # region lemmatization
    def do_apply_lemmatization_task(self, current_data: pd.DataFrame, column_name) -> pd.DataFrame :
        return current_data
    #endregion


