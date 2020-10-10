Python provides a wonderful built-in tool called `NamedTuple`. Let's go
ahead and import it:

`from typing import NamedTuple`{{execute windows}}

Now, what is a `NamedTuple`? It's a class you can extend, and it makes a
constructor for you. Let's create a simple class Animal, with an age and a
name.

```
class Animal(NamedTuple):
    age: int
    name: str
```{{execute windows}}

OK, great. Now let's test that the constructor works.

```
a = Animal(12, "Fido")
print(f"The animal {a.name} is {a.age} years old")
```{{execute windows}}

We could have written this class in the standard Python way as well:

```
class AnimalWithoutNamedTuple:
    def __init__(self, age, name):
        self.age = age
        self.name = name
```{{execute windows}}

We saved one whole line of code...which doesn't seem that impressive. But
one hidden advantage of named tuples is that they are immutable:

```
a1 = Animal(12, "Fido")
a1.age = 13
```{{execute windows}}

Fido's birthday will have to wait. But if we re-create this dog using the other
class, it will work!

```
a2 = AnimalWithoutNamedTuple(12, "Fido")
a2.age = 13
print(f"Happy {a2.age}th Birthday, {a2.name}")
```{{execute windows}}

Now we have one immutable class, and one mutable class. But it looks like we
can't do anything useful with the immutable class—we can't give animals
birthdays! Fortunately, `NamedTuple` includes a useful built-in method,
`_replace()`, which lets you copy a `NamedTuple` (or, more precisely, a class
extending `NamedTuple`) but with one field updated. Let's try it out:

```
birthday_pup = a1._replace(age=13)
print(f"Happy {birthday_pup.age}th Birthday, {birthday_pup.name}")
```{{execute windows}}

That's pretty neat! Now we have data that is immutable, but we can also create
different versions of it to keep track of change over time. Now we don't have
to write getters and setters or constructors, and people looking at our code
will immediately know that our data structures are immutable.
