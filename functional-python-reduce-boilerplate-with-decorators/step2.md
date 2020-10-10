The first decorator we'll write will print `'decorator used'` whenever the
function it decorates is called. First, let's write the decorator, then we can
use it on some functions.

First, run the following code snippet by clicking on it, in order to start
Python.

```
python3
```{{execute windows}}

We have to define a decorator, which will take in a function to modify.
Let's call it `print_test`, because it's testing that decorators work by
printing something, and name the function `func`, which is conventional.

```
def print_test(func):
    def modified(*args, **kwargs):
        print('decorator used')
        return func(*args, **kwargs)
    return modified

```{{execute windows}}

This function will print `'decorator used'` and then return whatever the
function it is decorating returned. The `*args, **kwargs` bit means that
whatever inputs you provided (arguments or keyword arguments) will be passed
to the inner function.

We can test our decorator by first defining a decorated function:

```
@print_test
def f(x):
    return x + 3

```{{execute windows}}

And then calling that function:

```
f(4)
```{{execute windows}}

Great! That's a basic decorator, which wraps a function and modifies
it. In the next section, we will write a more useful decorator.
