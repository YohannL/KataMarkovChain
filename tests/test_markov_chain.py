"""
Project: katamarkovchain
Module: tests
file: test_markov_chain.py
Class: TestMarkovChain
"""
import pytest
from katamarkovchain.core.markovchain import MarkovChain


class TestMarkovChain:
    """
    pytest class with all tests
    """
    @staticmethod
    def test_init_markov():
        """
        Test the creation of Markov Object
        :return:
        """
        word = "test"
        markovchain = MarkovChain(word)
        assert word == markovchain.word

    @staticmethod
    def test_get_self():
        """
        Test the function get
        :return:
        """
        word = "test"
        markovchain = MarkovChain(word)
        assert markovchain.get_self() is markovchain

    @staticmethod
    def test_add_new_transitions():
        """
        Test the function to add new transitions
        :return:
        """
        markovchain1 = MarkovChain('test1')
        markovchain2 = MarkovChain('test2')
        markovchain1.add_transition(markovchain2.get_self())
        assert markovchain1.transition_state[markovchain2.get_self()] == 1
        markovchain3 = MarkovChain('test3')
        markovchain1.add_transition(markovchain3.get_self())
        assert markovchain1.transition_state[markovchain3.get_self()] == 1
        markovchain1.add_transition(markovchain2.get_self())
        assert markovchain1.transition_state[markovchain2.get_self()] == 2

    @staticmethod
    @pytest.fixture
    def test_get_transition(mocker):
        """
        Test to get transition
        :param mocker:
        :return:
        """
        markovchain1 = MarkovChain('test1')
        markovchain2 = MarkovChain('test2')
        markovchain3 = MarkovChain('test3')
        markovchain1.add_transition(markovchain2.get_self())
        assert markovchain1.get_next_transition() is markovchain2
        markovchain1.add_transition(markovchain3.get_self())

        mocker.patch('core.MarkovChain.generator_random_number',
                     return_value=1)
        assert markovchain1.get_next_transition() is markovchain2
        mocker.patch('core.MarkovChain.generator_random_number',
                     return_value=2)
        assert markovchain1.get_next_transition() is markovchain3
