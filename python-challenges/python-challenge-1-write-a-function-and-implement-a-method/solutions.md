Change step1.py to be:
```python
def get_dog(dictionary):
    return dictionary['dog']
```

Change step2.py to be:
```
def get_table(txt):
    """This function returns a dictionary such that dictionary[letter][next] is equal to
    the number of times that `letter` came before `next` in the input `txt`.

    >>>get_table('ab')
    {'a': {'b': 1}}
    """
    results = {}
    for i in range(len(txt)):
        current = txt[i]
        try:
            next = txt[i + 1]
        except IndexError:
            break

        if current in results:
            transitions = results[current]
        else:
            transitions = {}

        if next not in transitions:
            transitions[next] = 1
        else:
            transitions[next] += 1
            pass
        results[current] = transitions

    return results

```

Change step3.py to be
```python
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
                possibles.append(key)
        return random.choice(possibles)
```

Change step4.py to be
```
def get_table(txt):
    """This function returns a dictionary such that dictionary[letter][next] is equal to 
    the number of times that `letter` came before `next` in the input `txt`.
    
    >>>get_table('ab')
    {'a': {'b': 1}}
    """
    results = {}
    for i in range(len(txt)):
        current = txt[i]
        try:
            next = txt[i+1]
        except IndexError:
            break
            
        transitions = results.get(current, {})
        transitions.setdefault(next, 1)
            
        results[current] = transitions
        
    return results
```
