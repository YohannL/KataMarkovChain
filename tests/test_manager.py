"""
Project: katamarkovchain
Module: tests
file: test_manager.py
Class: TestManager
"""
from katamarkovchain.core.manager import Manager


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
    def test_manager_run(mocker):
        """
        test TODO
        :return:
        """
        manager = Manager()
        mocker.patch.object(manager, 'creation_all_mv')
        manager.run("This is a test.")
        # pylint: disable=maybe-no-member
        manager.creation_all_mv.assert_called_with("This is a test.")
        assert True

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
