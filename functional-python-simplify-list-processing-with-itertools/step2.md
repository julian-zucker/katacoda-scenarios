Itertools will let us create and modify iterators. Let's start with creating
iterators, so we have examples readily available to us in the next sections.

Let's import itertools.

```
from itertools import *
```{{execute}}

The first tool we'll look at is `repeat`, which takes in a value and a number,
and produces an iterator containing that value that many times. Here's an
example.

```
list(repeat(10, 3))
```{{execute}}

We still have to wrap the output in `list` in order to see the elements, but
it is clear that the above code repeats 10 three times. Next let's move on to
`islice`, which slices an iterator, taking only the first `n` elements, or a
range if two numbers are provided.


```
list(islice(repeat(10, 10), 3)
```{{execute}}

Here, we take only the first three elements from the `repeat` object, which
would have 10 elements otherwise. And, we can take the fourth through seventh
objects just as easily:

```
list(islice(repeat(10, 10), 4, 7)
```{{execute}}

Although because it's all 10's, there is no difference between the two. Now that
we know how to get elements out of an iterator, we can start playing with
infinite iterators.

One way of creating an infinite iterator is `count`. `count` starts at
whatever number you give it, and gives you back an iterator with that number
as the first element, that number plus one as the second element, plus two,
plus three, and so one. Let's try it out

```
list(islice(count(10), 12))
```{{execute}}

Even though the iterator is technically infinite, it won't cause any problems
if we only take a fixed number of elements with islice. If we tried to write a
for loop that went over the whole thing, however, it would run forever.

Another method for making infinite generators is `cycle`. `cycle` takes in an
iterable (like a string or an array) and produces an iterator that cycles
through its elements.

```
list(islice(cycle("ABCD"), 12))
```{{execute}}

The above code repeats the letters of `"ABCD"`, and take the first 12 of them.

Once you have a finite iterable, you can combine its elements to make new
iterators. One of the "combinatoric" iterators is called `product`. It
produces the cartesian produce of two iterators, creating every pair
containing one element of the first iterator and one element of the second
iterator. Here's an example:

```
list(product([1, 2, 3, 4], "ABC"))
```{{execute}}

You can also get the product of an iterator with itself:

```
list(product("ABC", repeat=2))
```{{execute}}

Although notice that you have to specify `repeat=2` in order to get tuples
with two elements in them.

You can also create the permutations and combinations of the elements of an
iterable:

```
list(permutations([1, 2, 3]))
```{{execute}}

For combinations, you have to provide the length of each combination that you
want.
```
list(combinations("ABCDE", r=2))
```{{execute}}

These combinators are useful for double-checking your combinatorics math
homework, and also seeing if any combination of elements has a certain
property, which can be useful in several leetcode exercises.

That's a lot of ways to create iterables! With this knowledge under our belts,
we can move to the next step, where we will dive into ways to use iterables.
