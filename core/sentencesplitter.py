"""
Project: katamarkovchain
Module: Core
file: sentencesplitter.py
Function: sentencesplitter
"""
import re


def sentencesplitter(sentence):
    """
    To split a sentence
    :param sentence: Sentence to split
    :return: list of the seperate words
    """
    return re.findall(r"[\w']+|[.,!?;]", sentence)
