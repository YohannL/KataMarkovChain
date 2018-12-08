"""
Project: katamarkovchain
Module: Core
file: manager.py
Class: manager
"""
from katamarkovchain.core.markovchain import MarkovChain
from katamarkovchain.core.sentencesplitter import SentenceSplitter


class Manager:
    """
    Manager class will manager all process
    """

    def __init__(self):
        """
        Standard initialization
        """
        self.markovchainlist = {}
        self.sentencesplitter = SentenceSplitter()

    def create_new_mv(self, word):
        """
        Given a word, will check if this word is in markovchinlist,
        otherwise it will create and add a new one
        :param word: given word to find the MV object
        :return: pointer of the makov chain object
        """
        found_mv = None
        if self.markovchainlist.get(word.lower()):
            found_mv = self.markovchainlist.get(word.lower())
        else:
            found_mv = MarkovChain(word.lower())
            self.markovchainlist[word.lower()] = found_mv
        return found_mv

    def creation_all_mv(self, text):
        """
        _creation_all_mv function to create all marlov chain
        with their links
        :param text:
        :return:
        """
        list_sentence = self.sentencesplitter.run(text)
        start_mv = MarkovChain(None)
        self.markovchainlist[None] = start_mv
        previous_mv = start_mv
        for word in list_sentence:
            actual_mv = self.create_new_mv(word)
            previous_mv.add_transition(actual_mv)
            previous_mv = actual_mv

    def run(self, text):
        """
        Run function will call the splitter function and
        create markov chain list
        :param text: to split and to create markov chain
        :return:
        """
        self.creation_all_mv(text)
