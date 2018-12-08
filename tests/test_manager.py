"""
Project: katamarkovchain
Module: tests
file: test_manager.py
Class: TestManager
"""
from katamarkovchain.core.manager import Manager
from katamarkovchain.core.markovchain import MarkovChain


class TestManager:
    """
    pytest class with all tests
    """

    @staticmethod
    def test_create_new_mv():
        """
        Test the creation of one markov chain
        :return:
        """
        manager = Manager()
        new_mv = manager.create_new_mv("test")
        assert new_mv is not None
        assert new_mv.word == "test"

    @staticmethod
    def test_create_unique_new_mv():
        """
        Test the unicity of two markov chain objects with the same word
        :return:
        """
        manager = Manager()
        new_mv_1 = manager.create_new_mv("test")
        new_mv_2 = manager.create_new_mv("test")
        assert new_mv_1 is not None
        assert new_mv_1.word == "test"
        assert new_mv_2 is not None
        assert new_mv_2.word == "test"
        assert new_mv_1 is new_mv_2

    @staticmethod
    def test_manager_run_called_creation(mocker):
        """
        test
        :return:
        """
        manager = Manager()
        mocker.patch.object(manager, 'creation_all_mv')
        manager.run("This is a test.")
        # pylint: disable=maybe-no-member
        manager.creation_all_mv.assert_called_with("This is a test.")

    @staticmethod
    def test_manager_run_called_generator_if_link_created(mocker):
        """
        test
        :return:
        """
        manager = Manager()
        mocker.patch.object(manager, 'generator_text')
        manager.run("This is a test.")
        # pylint: disable=maybe-no-member
        manager.generator_text.assert_called_with(0)

    @staticmethod
    def test_manager_run_no_called_generator_if_links_no_created(mocker):
        """
        test
        :return:
        """
        manager = Manager()
        mocker.patch.object(manager, 'generator_text')
        manager.run(None)
        # pylint: disable=maybe-no-member
        manager.generator_text.assert_not_called()

    @staticmethod
    def test_manager_run_no_called_generator():
        """
        test
        :return:
        """
        manager = Manager()
        mv_start = MarkovChain(None)
        mv_this = MarkovChain("this")
        mv_is = MarkovChain("is")
        mv_a = MarkovChain("a")
        mv_test = MarkovChain("test")
        mv_point = MarkovChain(".")

        mv_start.add_transition(mv_this)
        mv_this.add_transition(mv_is)
        mv_is.add_transition(mv_a)
        mv_a.add_transition(mv_test)
        mv_test.add_transition(mv_point)
        mv_point.add_transition(mv_start)

        manager.markovchainlist[None] = mv_start
        manager.markovchainlist[mv_this.word] = mv_this
        manager.markovchainlist[mv_is.word] = mv_is
        manager.markovchainlist[mv_a.word] = mv_a
        manager.markovchainlist[mv_test.word] = mv_test
        manager.markovchainlist[mv_point.word] = mv_point

        generated_text = manager.generator_text(1)
        assert generated_text == "this is a test."

    @staticmethod
    def test_creation_all_mv_called_splitter(mocker):
        """
        test creation_all_mv_called_splitter function
        :return:
        """
        manager = Manager()
        sentencesplitter = manager.sentencesplitter
        mocker.patch.object(sentencesplitter, 'run')
        manager.creation_all_mv("This is a test.")
        # pylint: disable=maybe-no-member
        sentencesplitter.run.assert_called_with("This is a test.")

    @staticmethod
    def test_creation_all_mv_called_create_new_mv(mocker):
        """
        test creation_all_mv_called_create_new_mv function
        :return:
        """
        manager = Manager()
        mocker.patch.object(manager, 'create_new_mv')
        manager.creation_all_mv("This is a test.")
        # pylint: disable=maybe-no-member
        manager.create_new_mv.assert_called()
