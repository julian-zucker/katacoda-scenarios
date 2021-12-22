In the previous challenge, you wrote the function `get_table`. Let's look at that code again.

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

Now let's update the code to use that parameter. Instead of just getting one element at time from the string, you can use the "slice" notation to get multiple letters at once.
```python
str = "abcdefg"
str[1:3]
# equals "bcd"
```

Now, you can open `step1.py`. Modify the function `get_table` to use the size parameter to take sections of the string for `current`, and grab the letter after that for `next`.