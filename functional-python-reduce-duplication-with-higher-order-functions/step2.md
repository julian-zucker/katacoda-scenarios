We want to write a function that will let us easily mass-produce functions
which add different numbers. We need this function to take as its input a
number, and return a function which adds that number. Here's how it's done:

```
def make_adder(n):
    def adder(x):
        return x + n
    return adder

```{{execute windows}}

OK, let's break down that code snippet. `make_adder` takes one parameter,
`n`, and then uses that parameter in a function it defines. The function
`adder`, which is defined locally within `make_adder`, stores that value of
`n`. `adder` is returned, and `adder` is a function that takes a number `x` and
adds `n` to it. Success!

How do we use this thing, though? Well, it's a function, so we can call it:

```
add_four = make_adder(4)
```{{execute windows}}

And then we can use the function we created!

```
assert add_four(0) == 4
assert add_four(4) == 8
```{{execute windows}}

We can even call it directly after creating it, if we want:

```
assert make_adder(10)(30) == 40
```{{execute windows}}

Now we know how to define higher-order functions that return functions. What
about higher-order functions that take functions as their input?
