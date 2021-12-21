import random
from step2 import get_table

class Markov:
    def __init__(self, txt):
        self.table = get_table(txt)

    def predict(self, letter):
        """Predicts which letter should come after the given letter."""
        options = self.table[letter]
        possibles = []
        for key in options:
            value = options[key]
            for i in range(value):
                # TODO for you
        return random.choice(possibles)
