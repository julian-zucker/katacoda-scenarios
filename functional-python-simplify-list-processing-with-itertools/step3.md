One Scala function that I often miss in Python is `tabulate`, which takes a
function and a number, and applies the function to each number from 0 up to
that number. So given `lambda x: x + 1` and `4`, it would return `1, 2, 3, 4`.
To write that function, we can use `count` to generate the numbers, `map`
to apply the function, and `islice` to take the first `n`, like so:

```
def tabulate(function, n):
    return islice(map(function, count()), n)

```{{execute windows}}

And a test:

```
list(tabulate(lambda x: x + 1, 4))
```{{execute windows}}

We could also do this with `range` and a list comprehension:

```
def tabulate2(function, n):
    return (function(n) for i in range(n))

```{{execute windows}}

We can test this, which will reveal the bug:

```
list(tabulate2(lambda x: x + 1, 4))
```{{execute windows}}

In the prior example, it should say `return (function(i) ...` instead of `return
(function(n) ...`, but because we had to mess around with variables ourselves,
it was possible to make this mistake. For simple mistakes like this, an IDE
would usually let us know that `i` was unused, but more complex mistakes in
iterable-processing code can be hard to miss.

To drive the point home, let's make an n-dimensional tabulate. You give it a
list of numbers, and it applies the given function to `(0, 0, 0), (0, 0, 1),
... (0, 0, n2), ... (n0, n1, n2)`.

First, we'll need a diversion into the function `starmap`. `starmap` is like
`mapv, but if you give it a tuple, it will pass the elements into the function
individually. An example might help make this clearer:

```
list(starmap(max, [[1, 2, 3], [4, 5, 6]]))
```{{execute windows}}

Max is being called on `max(1, 2, 3)`, then `max(4, 5, 6)`, even though the
list contains arrays. If we just used `map`, it would get called like `max([1, 2, 3])`, which would cause errors.

We can use `starmap` to tabulate the given function more than three numbers at
once.

First, an example function:
```
def func(x, y, z):
    return (x, y, z, x + y + z)

```{{execute windows}}

And now, we can develop the n-dimensional tabulate.

```
def tabulate_n_dimensional(function, *dimensions):
    # this contains 0, 1, ..., dimension for each dimension
    dimension_ranges = map(lambda dimension: list(islice(count(), dimension)), dimensions)
    # [(0, 0, 0), (0, 0, 1), ...
    inputs = product(*dimension_ranges)
    return starmap(function, inputs)

```{{execute windows}}

Let's test this:

```
list(tabulate_n_dimensional(func, 3, 4, 5))
```{{execute windows}}

As you can see, it worked on each tuple from (0, 0, 0) to (3, 4, 5). And it
required so little code!
