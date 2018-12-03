from random import randint


def generator_random_number(min, max):
    return randint(min, max)


class MarkovChain:

    def __init__(self, word: str):
        self.word = word
        self.transition_state = {}

    def add_transition(self, new_transition):
        if new_transition in self.transition_state:
            self.transition_state[new_transition] += 1
        else:
            self.transition_state[new_transition] = 1

    def get_self(self):
        return self

    def get_next_transition(self):
        max_random = 0
        for key, value in self.transition_state.items():
            max_random += value

        random_next_gen = generator_random_number(1, max_random)
        for state, value in self.transition_state.items():
            print(state, value)
            random_next_gen -= int(value)
            if random_next_gen <= 0:
                return state
