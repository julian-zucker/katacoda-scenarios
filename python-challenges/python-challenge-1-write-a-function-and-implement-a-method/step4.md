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

In the `if` statement that starts with `if current in results`, we basically want to get the value under `current` and default to `{}` if it doesn't exist. That sounds like what `get` does, so let's rewrite it:

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

That got 4 lines down to 1! Nice. Next, we can use a feature called `setdefault` to set a value in a dictionary if it doesn't exist. 

For example:
```python
x = {'a': 3}
x.setdefault('a', 10)
x.setdefault('b', 10)
x
# {'a': 3, 'b': 10}
```
If the key isn't present, `setdefault` will set the key to the given value. If the key is present, it won't do anything.
Now, open up `step4.py` and change the final if statement to use `setdefault`!
