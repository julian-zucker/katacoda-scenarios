In this step, we'll work on making a REPL, which is short for Read, Evaluate, Print, Loop.

This code will read the user's input, predict the next letter, and then print the prediction. It will do this in an infinite loop until the user chooses to exit.

First, we'll need a function that prints a welcome message.
```python
def repl(m):
    print("Welcome to the REPL!")
    print("Hit Ctrl-C to exit.")
```

Ok, that function looks good. Now we'll want to read a user's input, make a prediction, and print the prediction.

```python
def repl(m):
    print("Welcome to the REPL!")
    print("Hit Ctrl-C to exit.")

    txt = input("> ")
    prediction = m.predict(txt) 
    print(prediction)
```

Let's try running this function.

```python
m = Markov('abcdefgh', size=4)
repl(m)
```

That handles Read, Evaluate, and Print, but what about Loop? For that, we'll need to use a `while` loop.
```python
def repl(m):
    print("Welcome to the REPL!")
    print("Hit Ctrl-C to exit.")

    while True:
        txt = input("> ")
        prediction = m.predict(txt) 
        print(prediction)
```

If you run this command, you'll be able to enter multiple commands in a row. Try starting with a letter, and then adding whichever prediction was returned to see what letter comes third!

```python
repl(m)
```

If you try putting in something longer than the `size` of your markov chain, you'll see an `IndexError`, because there is no table of the right size. We'll want to handle that slightly better by adding some error handling.

```python
def repl(m):
    print("Welcome to the REPL!")
    print("Hit Ctrl-C to exit.")

    while True:
        txt = input("> ")
        try:
            prediction = m.predict(txt) 
        except IndexError:
            print("Too long, try again with a shorter input")
        else:
            print(prediction)
```

The `else` block is something special to Python. The `else` block is only executed if there is no exception. We need to put the print statement in an `else` block so that we don't try to reference `prediction` before it is defined.
