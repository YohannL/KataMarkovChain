"""
Project: katamarkovchain
Module: Core
file: sentencesplitter.py
class: SentenceSplitter
"""
import re


class SentenceSplitter:
    """
    SentenceSplitter class to split a sentence
    """

    # pylint: disable=too-few-public-methods
    # pylint: disable=no-self-use
    def run(self, sentence):
        """
        To split a sentence
        :param sentence: Sentence to split
        :return: list of the seperate words
        """
        return re.findall(r"[\w']+|[.,!?;]", sentence)
