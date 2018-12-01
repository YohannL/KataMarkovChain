from KataMarkovChain.Core.TextSplitter import TextSplitter


class TestTextSplitter():

    @staticmethod
    def test_split_one_sentence_without_coma():
        sentence = "Hey i am a test"
        assert TextSplitter.split(sentence) == ["Hey", "i", "am", "a", "test"]