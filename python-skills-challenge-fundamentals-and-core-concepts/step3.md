Now that we have `get_table` defined, we can try to predict the next letter based on that.

First, a recap on arrays. To add an item to an array, use the `append` method.
```python
x = []
x.append(1)
x.append(3)
assert x == [1, 3]
```

Let's start by defining a class called `Markov` that will make predictions.

```python
class Markov:
    pass
```

This class needs to have a constructor method, so that we can give it the text that it is predicting from.

```python
class Markov:
    def __init__(self, txt):
        self.table = get_table(txt)
```

Now, we can make a `Markov`, and look at the table for its input text:
```python
m = Markov('abcbc')
m.table
```

But we want more than just to access the table, we want to predict the next letter based on the previous letters! Let's
add a method called `predict`.

```python
class Markov:
    def __init__(self, txt):
        self.table = get_table(txt)

    def predict(self, letter):
        """Predicts which letter should come after the given letter."""
        pass
```

This method should return a random letter that has a transition from the given letter in the table. We can do this by building a list of possible choices, and the picking at random. If we add each letter to the list of possible choices once for each time the transition happened in the input string, we'll even have the predictions be weighted by frequency!

Open `step3.py` and add the necessary line of code to insert the correct key into the possibles array. 

Then try out some predictions.
```python
m = Markov('abcbcbcbcbcbd')
m.predict('a')
m.predict('b')
m.predict('b')
```

If you predict `'b'` long enough, you'll see that this code sometimes transitions to `'d'` but usually transitions to `'c'`. That's a working Markov chain!