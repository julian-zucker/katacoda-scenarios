First, let's recap how to use dictionaries in Python. A dictionary is Python's name for what other languages call mappings, HashMaps, or associative arrays. Dictionaries store keys and values, and make looking up the value for a specific key very fast. Here is an example of a dictionary that associates animals to their descriptions. 
```python
animals = {
    'cat': 'carnivorous mammal',
    'dog': 'furry canine'
}
```

The dictionary `animals` lets you look up the definitions of animals - just like a real dictionary! To access values, you can use square brackets `[]`.
```python
animals['cat']
```

And to add keys, we can just assign to the dictionary after accessing the key.
```python
animals['parrot'] = 'talking bird'
```

What happens if we try to access a key of a dictionary that doesn't exist?
```python
animals['chicken']
```

We get a `KeyError`! To access keys we aren't sure about, we can use the method `get`, and provide a default.
```python
animals.get('chicken', 'missing')
```

Now that you know about dictionaries, fill out the body of the `get_dog` function, so that it returns whatever value is under the key `"dog"` in the input.

