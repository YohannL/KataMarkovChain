from KataMarkovChain.Core.MarkovChain import MarkovChain, generator_random_number
import pytest


class TestMarkovChain:

    @staticmethod
    def test_init_markov():
        word = "test"
        markovchain = MarkovChain(word)
        assert word == markovchain.word

    @staticmethod
    def test_get_self():
        word = "test"
        markovchain = MarkovChain(word)
        assert markovchain.get_self() is markovchain

    @staticmethod
    def test_add_transitions():
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
    def test_get_newt_transition(mocker):
        markovchain1 = MarkovChain('test1')
        markovchain2 = MarkovChain('test2')
        markovchain3 = MarkovChain('test3')
        markovchain1.add_transition(markovchain2.get_self())
        assert markovchain1.get_next_transition() is markovchain2
        markovchain1.add_transition(markovchain3.get_self())

        mocker.patch('Core.MarkovChain.generator_random_number', return_value=1)
        for i in range(1000):
            assert markovchain1.get_next_transition() is markovchain2
        mocker.patch('Core.MarkovChain.generator_random_number', return_value=2)
        for i in range(1000):
            assert markovchain1.get_next_transition() is markovchain3
