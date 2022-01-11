Let's add `size` to the Markov class! When a size is provided, let's make a list of all tables from size 1 up to
the given size.

```python

import random 

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
```

Now, go ahead and open `step2.py`. Modify `predict` to pick the right table based on the size of its input. If it's given a single letter, it should make the prediction using the table with size 1, and if it's given three letters, it should use the table of size 3.
