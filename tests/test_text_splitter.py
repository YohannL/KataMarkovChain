from KataMarkovChain.Core.TextSplitter import TextSplitter


class TestTextSplitter:

    @staticmethod
    def test_split_one_sentence_without_coma():
        sentence = "Hey i am a test"
        assert TextSplitter.split(sentence) == \
               ["Hey", "i", "am", "a", "test"]

    @staticmethod
    def test_split_one_coma_sentence():
        sentence = "Hey i am a test."
        assert TextSplitter.split(sentence) == \
               ["Hey", "i", "am", "a", "test", "."]

    @staticmethod
    def test_split_two_coma_sentence():
        sentence = "Hey i am a test. Another one"
        assert TextSplitter.split(sentence) == \
               ["Hey", "i", "am", "a", "test", ".", "Another", "one"]
