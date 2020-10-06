Decorators are functions that modify other functions. They're called
"decorators" because they take some core functionality and add a little
decoration. Here's an example from statsd:

```
@statsd.timer('myfunc')
def myfunc():
    ...
```

In this example, we have a function that we want to "decorate" by adding a
timer to it. This timer will report the time the functions takes to call to
some server we've set up elsewhere. The important part is that we don't have
to modify our function at all in order to add timing to it. We can essentially
wrap it in a call to `statsd.timer`, and we're set!

Let's talk about the syntax for a second. There are two parts to that
definition. First, there is a normal function definition (the part that starts
with `def` and goes to thte end of the code block). Second, there is the
application of the decorator, which is the whole line starting with `@`. The
decorator takes in the function that is being defined, and modifies it, but
the function ends up with the same name.

This is equivalent to writing the following:

```
def timer():
    ...

def myfunc_without_timing():
    ...

myfunc = timer(myfunc_without_timing)
```

In this case, it's more obvious that the timer function is being called on
`myfunc_without_timing`. But `myfunc` will be exactly the same in the
following code snippet:

```
@timer()
def myfunc():
    ... # the same body as myfunc_without_timing above
```


In general, this:

```
@decorator
def function():
    ...
```

Will always be the same as this:
```
def temp_function():
    ...

function = decorator(function)
```

Now that we know how to use decorators, let's move on to writing our own!
