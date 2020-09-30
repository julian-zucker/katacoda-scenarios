Functions can take other functions as their input. If you've ever used filter
or map, you've given a function to another function. But how do you define
those functions yourself?

Turns out, you define it just like any other function, but what you do with
the parameters is different. Let's give it a shot by writing a function
`apply` which takes a function named `f` and calls that function on an
argument `arg`.

```
def apply(f, arg);
    return f(arg)

assert apply(add_three, 4) == 7
assert apply(add_four, 8) == 12
```{{execute}}

This is a pretty silly function because `apply(f, arg)` is the same as
`f(arg)`, but it requires more typing. However, it's a useful example: we can see
that f (the input) is being called like a normal function on another one of
the inputs.

We can do some more interesting things, though. Here's a function,
`filter_map`, that takes a list, a predicate (which is a function that will
return a boolean), and a mapping function, and first filters the list (keeping
only the items in the list that make the predicate return True) and then
applies the mapping function to each other element.

```
def filter_map(arr, predicate, mapper):
    out = []
    for item in arr:
        if predicate(item):
            new_item = mapper(item)
            out.append(new_item)

    return out

assert filter_map([1,2,3,4], lambda x: x > 2, add_three) == [6, 7]
```{{execute}}

Or, written another way:

```
def filter_map(arr, predicate, mapper):
    return [mapper(item) for item in arr if predicate(item)]

assert filter_map([1,2,3,4], lambda x: x > 2, add_three) == [6, 7]
```{{execute}}

`filter_map` could be useful in some scenarios, but list comprehensions will
probably be more useful. In the next step, we'll look at some more practical
examples.
