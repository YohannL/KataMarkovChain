"""
Project: katamarkovchain
Module: tests
file: test_manager.py
Class: TestManager
"""
from katamarkovchain.core.manager import Manager

SPLIT_PATH = "katamarkovchain.core.TextSplitter.TextSplitter.split"


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
    def test_manager_run():
        """
        test TODO
        :return:
        """
        manager = Manager()
        manager.run("This is a test.")
        assert True
