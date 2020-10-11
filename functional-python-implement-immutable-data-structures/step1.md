_Mutable data structures_ can be "mutated," or changed. _Immutable data
structures_ cannot be changed. This is useful for parallel programming, where
you want to prevent multiple people from modifying a piece of data at the same time, and in preventing bugs.

Before we dive into coding things, run `python3`{{execute windows}} so that we can use Python. (You can run things by clicking on the text.)

What's the difference between arrays and tuples? Well, I'm sure you've used arrays like this before:

```python
arr = [1, 2, 3]
arr[0] = -100
print(arr)
```{{execute windows}}

That second line, `arr[0] = -100`, means that the array is mutable. We can
change its elements, which is useful, but also means that people who are using
the array at the same time as us have to put up with our changes. Tuples, on the
other hand, behave differently. Click the following code to see what it does:

```
tup = (1, 2, 3)
tup[0] = -100
print(tup)
```{{execute windows}}

Tuples can't be modified! Once you have a tuple, you know that it won't be
changing on you. One exception: tuples can contain mutable elements, like
arrays. Run the following code to see how this leads to mutability:

```
tup = ([0], [1], [1, 2])
tup[0][0] = "I just got mutated!"
print(tup)
```{{execute windows}}

So while our tuples can't be mutated, their elements can. The solution? Make
their elements tuples as well! This can be accomplished by changing the square
brackets (`[]`) to parentheses (`()`):

```
tup = ((), (1), (1, 2))
tup[0][0] = "I just got mutated!"
print(tup)
```{{execute windows}}

So while tuples are immutable, arrays are mutable. We can use this fact to
make immutable data structures, as you'll see in the next section.
