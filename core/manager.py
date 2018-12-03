"""
Project: katamarkovchain
Module: Core
file: manager.py
Class: manager
"""
from katamarkovchain.core.markovchain import MarkovChain
from katamarkovchain.core.sentencesplitter import sentencesplitter


class Manager:
    """
    Manager class will manager all process
    """
    def __init__(self):
        """
        Standard initialization
        """
        self.markovchainlist = []

    def create_new_mv(self, word):
        """
        Given a word, will check if this word is in markovchinlist,
        otherwise it will create and add a new one
        :param word: given word to find the MV object
        :return: pointer of the makov chain object
        """
        found_mv = None
        for mv_element in self.markovchainlist:
            if mv_element.word is not None and\
                    mv_element.word.lower() == word.lower():
                found_mv = mv_element
        if not found_mv:
            found_mv = MarkovChain(word.lower())
            self.markovchainlist.append(found_mv)
        return found_mv

    def run(self, text):
        """
        Run function will call the splitter function and
        create markov chain list
        :param text: to split and to create markov chain
        :return:
        """
        list_sentence = sentencesplitter(text)
        start_mv = MarkovChain(None)
        self.markovchainlist.append(start_mv)
        previous_mv = start_mv
        for word in list_sentence:
            actual_mv = self.create_new_mv(word)
            previous_mv.add_transition(actual_mv)
            previous_mv = actual_mv
