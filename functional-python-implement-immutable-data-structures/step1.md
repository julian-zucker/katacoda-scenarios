Mutable data structures can be "mutated", or changed. Immutable data
structures cannot be changed. This is useful for parallel programming, where
you want to prevent multiple people from modifying a piece of data at the same time, and in preventing bugs.

Before we dive into coding things, run `ipython3`{{execute}} so that we can use Python. (You can run things by clikcing on their text).

What's the difference between arrays and tuples? Well, I'm sure you've used arrays like this before:

```python
arr = [1, 2, 3]
arr[0] = -100
print(arr)
```
{{execute}}


That second line, `arr[0] = -100`, means that the array is mutable. We can
change its elements, which is useful, but also means that people who are using
the array at the same as us have to put up with our changes. Tuples, on the
other hand, behave differently. Click the code below to see what it does:

```
tup = (1, 2, 3)
tup[0] = -100
print(tup)
```{{execute}}

Tuples can't be modified! Once you have a tuple, you know that it won't be
changing on you. One exeption: tuples can contain mutable elements, like
arrays. Run the code below to see how this leads to mutability.

```
tup = ([0], [1], [1, 2])
tup[0][0] = "I just got mutated!"
print(tup)
```{{execute}}

So while our tuples can't be mutated, their elements can. The solution? Make
their elements tuples as well!

```
tup = ((), (1), (1, 2))
tup[0][0] = "I just got mutated!"
print(tup)
```{{execute}}

So while our Tuples are
