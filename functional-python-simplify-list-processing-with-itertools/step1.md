The most fundamental tools for operating on iterators are `map` and `filter`.
`map` allows you to apply a function to each element of a list, and filter
allows you to keep only the elements of the list that make a function return
true. Let's play around with them both to get familiar.

First, `map`. Suppose we have a list of numbers, and we want to add 3 to each of
them. How could we achieve that? Well, `map` will let us apply a function to
each element of the list. What function do we want to apply? The function that
will add 3. Let's start up Python:

```
python3
```{{execute windows}}

And then let's define that function!

```
def add_three(x):
    return x + 3

```{{execute windows}}

Now that we have this function, let's write down the list we want to apply it
to.

```
arr = [1, 2, 3, 4]
```{{execute windows}}

Finally, we can use `map` to apply the function to each element:

```
map(add_three, arr)
```{{execute windows}}

That doesn't look quite right. It's a `map` object instead of a list? Python's
map is implemented in this way so that it can improve the performance of some
operations on the resulting object. For example, if you map over a list twice,
you might not want the intermediate list to be created, if you can just apply
the two functions to each element in one pass. We can fix this by wrapping it
all in a call to `list`, to convert the type again.

```
list(map(add_three, arr))
```{{execute windows}}

Much better: this is looking more like what I would expect. That's how
to use `map`! Next, on to `filter`.

Suppose you have a list of strings, but you only want the ones that are
lowercase. With filter, all you need to do is find or create a function that returns
`True` for the elements you want to keep, and returns `False` for the elements
that you don't want to keep. In our case, we will want to keep lowercase
strings and not keep strings with uppercase letters, so let's write that
function!

```
def is_lowercase(str):
    return str.islower()

```{{execute windows}}

This may seem like a silly function to write, because all it does is call one
other method, but `filter` requires a function, not a method, so we have to write it.

Let's just define our array of strings:
```
arr = ["low", "HIGH", "MiXeD"]
```{{execute windows}}

And then we can filter, keeping only the lowercase ones:

```
filter(is_lowercase, arr)
```{{execute windows}}

Oops! Same deal as above–this is a generator, so we'll have to convert it to
a list to see the contents.
```
list(filter(is_lowercase, arr))
```{{execute windows}}

And just like that, we know how to use `filter` and `map`! In the next step, we'll
focus on ways to create iterators.
