from KataMarkovChain.Core.MarkovChain import MarkovChain
from KataMarkovChain.Core.TextSplitter import TextSplitter


class Manager:
    def __init__(self):
        self.textsplitter = TextSplitter()
        self.markovchainlist = []

    def create_new_mv(self, word):
        found_mv = None
        for mv in self.markovchainlist:
            if mv.word is not None and\
                    mv.word.lower() == word.lower():
                found_mv = mv
        if not found_mv:
            found_mv = MarkovChain(word.lower())
            self.markovchainlist.append(found_mv)
        return found_mv

    def run(self, text):
        list_sentence = self.textsplitter.split(text)
        start_mv = MarkovChain(None)
        self.markovchainlist.append(start_mv)
        previous_mv = start_mv
        for word in list_sentence:
            actual_mv = self.create_new_mv(word)
            previous_mv.add_transition(actual_mv)
            previous_mv = actual_mv
