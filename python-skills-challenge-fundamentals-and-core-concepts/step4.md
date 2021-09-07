Let's revisit `get_table` and try to refactor it to make it simpler and easier to read. 

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
            
        if current in results:
            transitions = results[current]
        else:
            transitions = {}
            
        if next not in transitions:
            transitions[next] = 1
        else:
            transitions[next] += 1
        results[current] = transitions
        
    return results
```

In the if statement that starts with `if current in results`, we basically want to get the value under `current`, and default to `{}` if it doesn't exist. That sounds like what `get` does, so let's rewrite it:

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
            
        if next not in transitions:
            transitions[next] = 1
        else:
            transitions[next] += 1
        results[current] = transitions
        
    return results
```

That got 4 lines down to 1! Nice. Next, we can use a feature called `setdefault` to set a value in a dictionary if it doesn't exist. That will come in handy at the bottom of the function:
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
