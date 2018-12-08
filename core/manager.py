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
            if word == ".":
                actual_mv.add_transition(start_mv)
                previous_mv = start_mv

    def generator_text(self, number):
        """
        :param number:
        :return:
        """
        generated_text = ""
        actual_mv = self.markovchainlist[None]
        while number > 0:
            actual_mv = actual_mv.get_next_transition()
            if actual_mv.word == ".":
                generated_text += actual_mv.word
                actual_mv = self.markovchainlist[None]
                number -= 1
            elif generated_text == "":
                generated_text += actual_mv.word
            else:
                generated_text += " " + actual_mv.word
        return generated_text

    def run(self, text, numbersentences=0):
        """
        Run function will call the splitter function and
        create markov chain list
        :param text:
        :param numbersentences:
        :return:
        """
        if text:
            self.creation_all_mv(text)
            if self.markovchainlist:
                generated_text = self.generator_text(numbersentences)
                return generated_text
        return None
