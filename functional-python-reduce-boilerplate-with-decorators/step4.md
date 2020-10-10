Decorators are functions like any other. And the functions they wrap are also
just like every other function. This means that we can control what data gets
passed in, and modify what the wrapped function returns.

For example, here's a decorator which always calls its wrapped function with
4, regardless of what the input is. It also adds one to the output:

```
def call_with_four_and_increment_result(func):
    def modified(*args, **kwargs):
        return func(4) + 1
    return modified

```{{execute windows}}

And a quick test:

```
@call_with_four_and_increment_result
def f(x):
    return x + 1

print(f(6))
print(f(8))
print(f(9))
```{{execute windows}}

Awesome! This trick is quite useful for writing decorators that pass in
database sessions to other functions, or when you want to check some schema
against the input or output data.
