Replace step1.py with 
```python
import urllib.request as req

def fetch_url(url, file_name):
    file_in = req.urlopen(url)
    data = file_in.read()
    file_out = open(file_name, mode='wb')
    file_out.write(data)
    file_out.close()
```

replace step2.py with
```
import random

from step1 import fetch_url

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
        """Predicts which letter should come after the given letter."""
        options = self.tables[len(txt)-1][txt]
        possibles = []
        for key in options:
            value = options[key]
            for i in range(value):
                possibles.append(key)
        return random.choice(possibles)

def from_file(file_name, size):
with open(file_name, encoding='utf8') as file_in:
# Can you make this function return a Markov trained on the data in the given file?
return Markov(file_in.read())

FRANKENSTEIN_URL = "https://www.gutenberg.org/files/84/84-0.txt"
FRANKENSTEIN_FILE_NAME = 'frankenstein.txt'
fetch_url(FRANKENSTEIN_URL, FRANKENSTEIN_FILE_NAME)
```