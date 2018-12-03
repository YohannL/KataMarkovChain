from KataMarkovChain.Core.TextSplitter import TextSplitter


class TestTextSplitter:

    @staticmethod
    def test_split_one_sentence_without_coma():
        sentence = "Hey i am a test"
        expected_output = ["Hey", "i", "am", "a", "test"]
        assert TextSplitter.split(sentence) == expected_output

    @staticmethod
    def test_split_one_coma_sentence():
        sentence = "Hey i am a test."
        expected_output = ["Hey", "i", "am", "a", "test", "."]
        assert TextSplitter.split(sentence) == expected_output

    @staticmethod
    def test_split_two_coma_sentence():
        sentence = "Hey i am a test. Another"
        expected_output = ["Hey", "i", "am", "a", "test", ".", "Another"]
        assert TextSplitter.split(sentence) == expected_output
