In the previous skills challenge, you wrote the function `get_table`. Let's look at that code again.

```python
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
        transitions.setdefault(next, 0)
        transitions[next] += 1
        results[current] = transitions
        
    return results
```

This code is great, but if we want better predictions, we'll want to use more than just the previous letter. Let's work on adding a `size` parameter, which tells us how many previous letters to use. Let's make it default to 1.

```python
def get_table(txt, size=1):
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
        transitions.setdefault(next, 0)
        transitions[next] += 1
        results[current] = transitions
        
    return results
```

Now that we have our size parameter, let's look at the previous `size` letters, instead of just one.

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

Let's test out the new `get_table` function.

```python
get_table('abcbc', size=3)
```

In the next step, we'll make `predict` work with different sizes!
