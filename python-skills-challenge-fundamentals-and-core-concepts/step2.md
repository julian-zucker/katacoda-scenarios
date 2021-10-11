In this step, we will be implementing the function `get_table`. This function will allow us to build transition tables for our Markov chain.

```python
def get_table(txt):
    """This function returns a dictionary such that dictionary[letter][next] is equal to 
    the number of times that `letter` came before `next` in the input `txt`.
    
    >>>get_table('ab')
    {'a': {'b': 1}}
    """
    pass
```

We can build up this function over multiple steps. First, let's make it just return a dictionary at all:

```python3
def get_table(txt):
    """This function returns a dictionary such that dictionary[letter][next] is equal to 
    the number of times that `letter` came before `next` in the input `txt`.
    
    >>>get_table('ab')
    {'a': {'b': 1}}
    """
    results = {}
    return results
```

Now, we'll want to iterate over each character in the input text, so that we can each transition to our transition table. To iterate over the indexes of a string, we can use the `range` and `len` methods, to create a range from 0 up to the length of the string.

```python
def get_table(txt):
    """This function returns a dictionary such that dictionary[letter][next] is equal to 
    the number of times that `letter` came before `next` in the input `txt`.
    
    >>>get_table('ab')
    {'a': {'b': 1}}
    """
    results = {}
    for i in range(len(txt)):
        ...
    return results
```

But what should go in those `...`s? We want to look at this character, and the next character, and put those keys in the `results` dictionary. Let's start with a simplified version, that puts the number 1 in the transition table for transitions that exists, but doesn't know how to add beyond that.

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
        next = txt[i+1]
        results[current] = {next: 1}
        
    return results
```

Let's test this function a little and see how it does.

```python
get_table('abcbc')
```

Oh no! An `IndexError`! That's because when `i` is 2, at the end of the loop, we try to access `txt[3]`, which doesn't exist. To fix this, let's just stop iterating once we hit an `IndexError`.

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
            
        results[current] = {next: 1}
        
    return results
```

And let's test it out again.

```python
get_table('abcbc')
```

Sweet, it found the `a` to `b` transition! Now, we can work on increasing the count when we see the same thing multiple times. For that, we will want to check whether the transition we are writing already exists in the dictionary or not.

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
            # For you to do!
            pass
        else:
            # For you to do!
            pass
        results[current] = transitions
        
    return results
```

I filled in most of the function, but it's up to you to figure out what this code should do if `next` is either in or not in the transitions dictionary!


