import random
import sys


def get_table(txt, size=1):
    """This function returns a dictionary such that dictionary[letter][next] is equal to
    the number of times that `letter` came before `next` in the input `txt`.

    >>>get_table('ab')
    {'a': {'b': 1}}
    """
    results = {}
    for i in range(len(txt)):
        # change the next line to grab `size` characters using the [...:...] notation
        current = txt[i:i+size]
        try:
            # change this line to grab the letter after `current` ends
            next = txt[i+size]
        except IndexError:
            break

        transitions = results.get(current, {})
        transitions.setdefault(next, 0)
        transitions[next] += 1
        results[current] = transitions

    return results

class Markov:
    def __init__(self, txt, size=1):
        self.tables = []
        for i in range(size):
            self.tables.append(get_table(txt, size=i+1))

    def predict(self, txt):
        """Predicts which letter should come after the given text."""
        table = self.tables[len(txt) - 1]
        options = table[txt]
        possibles = []
        for key in options:
            value = options[key]
            for i in range(value):
                possibles.append(key)
        return random.choice(possibles)

def repl(m):
    print("Welcome to the REPL!")
    print("Hit Ctrl-C to exit.")

    while True:
        txt = input("> ")

        try:
            prediction = m.predict(txt)
            print(prediction)
        except IndexError:
            print("Input too long, try again with a shorter input.")

# TODO make main accept an argument called `txt`, and make a Markov based on that input.
def main():
    repl(...)


if __name__ == '__main__':
    main(sys.argv[1])
