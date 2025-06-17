import pandas as pd
import re

class CustomPipeline():
    def __init__(self):
        pass

    def detect_all_html_tags(self, data : pd.DataFrame, column_name: str) -> list[str]:
        all_tags :set[str] = set()
        for index, row in data.iterrows():
            text = row[column_name]
            tag_list = self.detect_html_tags(text)
            all_tags.update(tag_list)

        return all_tags


    def detect_html_tags(self, text : str) -> list[str]:
        balises = re.findall(r'</?(\w+)', text)
        return set(balises)
