"""
Project: katamarkovchain
Module: tests
file: test_sentence_splitter.py
Class: TestSentenceSplitter
"""
from katamarkovchain.core.sentencesplitter import SentenceSplitter


class TestSentenceSplitter:
    """
    pytest class with all tests
    """
    @staticmethod
    def test_split_one_sentence_without_coma():
        """
        Test the sentence splitter with a sentence WO coma
        :return:
        """
        sentence = "Hey i am a test"
        expected_output = ["Hey", "i", "am", "a", "test"]
        sentencesplitter = SentenceSplitter()
        assert sentencesplitter.run(sentence) == expected_output

    @staticmethod
    def test_split_one_coma_sentence():
        """
        Test the sentence splitter with a sentence W coma
        :return:
        """
        sentence = "Hey i am a test."
        expected_output = ["Hey", "i", "am", "a", "test", "."]
        sentencesplitter = SentenceSplitter()
        assert sentencesplitter.run(sentence) == expected_output

    @staticmethod
    def test_split_two_coma_sentence():
        """
        Test the sentence splitter with 2 sentences WO coma
        :return:
        """
        sentence = "Hey i am a test. Another"
        expected_output = ["Hey", "i", "am", "a", "test", ".", "Another"]
        sentencesplitter = SentenceSplitter()
        assert sentencesplitter.run(sentence) == expected_output
