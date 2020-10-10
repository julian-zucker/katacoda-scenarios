This step will introduce a problem to motivate the use of higher-order
functions. First, let's get a Python shell running:

`python`{{execute windows}}

Now, let's define a function.

```
def add_two(x):
    return x + 2

```{{execute windows}}

This is a pretty simple function. It takes a number `x` and returns that
number plus two. We can test it with some assertions:

```
assert add_two(0) == 2
assert add_two(1) == 3
```{{execute windows}}

(If you haven't seen assertions before: they won't do anything if the value
given to them is truthy, and they will raise an AssertionError otherwise.)

So we have this function. Let's define and test a similar function,
which adds three:

```
def add_three(x):
    return x + 3

assert add_three(0) == 3
assert add_three(100) == 103
```{{execute windows}}

These two functions are quite similar. While they are pretty small and were
easy to write, if we had to write dozens or hundreds of similar functions, it
would get tiring pretty fast!

This is where higher-order functions come in.
