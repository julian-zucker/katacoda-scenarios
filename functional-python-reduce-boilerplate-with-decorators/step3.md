One case where you might want to modify a function you've written is to add
logging. Perhaps you want to add a timer to the function, or you want to print
its inputs and outputs. While you should use a real
profiler and a real debugger, in this case, suppose we wanted to do a quick
hack to test a hypothesis.

We want to write a decorator that prints the duration of a function, and
prints its inputs and outputs. Let's start with just timing.


```
from datetime import datetime

def timing(func):
    def modified(*args, **kwargs):
        start_time = datetime.now()
        output = func(*args, **kwargs)
        print(f'{func.__name__} took {datetime.now() - start_time}')
        return output

    return modified
```{{execute}}

This function first records the starting time. Then, it calls the function
its decorating, and computes the difference between the current time (after
the function call) and the starting time. It prints that difference.


Let's try it out! First we'll need to define a function using the decorator:

```
from time import sleep

@timing
def sleepy(x, foo=None):
    sleep(1)
    return 3
```{{execute}}

Then, we can call it to see what we get.

```
sleepy(4)
sleepy(5)
```{{execute}}

Awesome! Now we have a decorator we can add to any function to record its
timing. This is quite useful when you have existing code you want to
instrument, and only requires a one-line change! Let's make a slightly better
version of this function, calling `debugging`, that also records the inputs
and outputs of the function.

```
from datetime import datetime

def debugging(func):
    def modified(*args, **kwargs):
        start_time = datetime.now()
        output = func(*args, **kwargs)
        print(f'{func.__name__} called on {args}, {kwargs}, returning {output}. It took {datetime.now() - start_time}.')
        return output

    return modified
```{{execute}}

And we can redefine sleepy with the new decorator

```
from time import sleep

@debugging
def sleepy(x, foo=None):
    sleep(1)
    return 3
```{{execute}}

And test it just like before:


```
sleepy(1)
sleepy("hello", foo="bar")
```{{execute}}

I've used functions like this to help me debug before. Hopefully knowing how
to use decorators can help you debug things too!

In the next section, we'll write a decorator that manipulates the input and
output of a function.
