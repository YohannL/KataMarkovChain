"""
Project: katamarkovchain
Module: Core
file: markovchain.py
Class: markovchain
"""
from random import randint


def generator_random_number(min_integer, max_integer):
    """
    Return a random integer between min and max
    :param min_integer: min integer
    :param max_integer: max integer
    :return:
    """
    return randint(min_integer, max_integer)


class MarkovChain:
    """
    Markov chain class is to manage data about the word and
    the possible transitions
    """
    def __init__(self, word: str):
        """
        Standard initialization
        :param word: Word to stock
        """
        self.word = word
        self.transition_state = {}

    def add_transition(self, new_transition):
        """
        Add a new transition to the current markov node
        :param new_transition: new transition to add
        :return:
        """
        if new_transition in self.transition_state:
            self.transition_state[new_transition] += 1
        else:
            self.transition_state[new_transition] = 1

    def get_self(self):
        """
        Return his pointer
        :return:
        """
        return self

    def get_next_transition(self):
        """
        Return a random transition
        :return: pointer on the next Markov Chain object
        """
        max_random = 0
        for value in self.transition_state.values():
            max_random += value

        random_next_gen = generator_random_number(1, max_random)
        for state, value in self.transition_state.items():
            random_next_gen -= int(value)
            if random_next_gen <= 0:
                return state
        return None
