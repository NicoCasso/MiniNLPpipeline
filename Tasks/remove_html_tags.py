import pandas as pd
import re
from pipeline_task import PipelineTask
from task_reference import TaskReference

class RemoveHtmlTags(PipelineTask):
    """
    input : a str column of the dataframe 
    output : a str column of the dataframe 
    """
    def __init__(self, column_name : str):
        super().__init__(TaskReference.REMOVEHTMLTAG, column_name)

    def do_work(self, current_data : pd.DataFrame) -> pd.DataFrame:
        current_data = self.remove_html_tags(current_data, self.column_name)
        detected_tags = self.detect_all_html_tags(current_data, self.column_name)
        for additionnal in detected_tags :
            specific_string = f"<{additionnal}"
            current_data = self.remove_specific(current_data, self.column_name, specific_string)

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