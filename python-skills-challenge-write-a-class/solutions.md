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