import random
from step1 import get_table

class Markov:
    def __init__(self, txt, size=1):
        self.tables = []
        for i in range(size):
            self.tables.append(get_table(txt, size=i+1))

    def predict(self, letter):
        """Predicts which letter should come after the given letter."""
        options = self.table[letter]
        possibles = []
        for key in options:
            value = options[key]
            for i in range(value):
                possibles.append(key)
        return random.choice(possibles)