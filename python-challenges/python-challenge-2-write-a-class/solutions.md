Change step1.py to

```python
def get_table(txt, size=1):
    """This function returns a dictionary such that dictionary[letter][next] is equal to
    the number of times that `letter` came before `next` in the input `txt`.

    >>>get_table('ab')
    {'a': {'b': 1}}
    """
    results = {}
    for i in range(len(txt)):
        current = txt[i:i+size]
        try:
            next = txt[i+size]
        except IndexError:
            break

        transitions = results.get(current, {})
        transitions.setdefault(next, 0)
        transitions[next] += 1
        results[current] = transitions

    return results

```

Change step2.py to
```python

import random
from step1 import get_table

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
```
