import re


class TextSplitter:
    @staticmethod
    def split(sentence):
        return re.findall(r"[\w']+|[.,!?;]", sentence)
