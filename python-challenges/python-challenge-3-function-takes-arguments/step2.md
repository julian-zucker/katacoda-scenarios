Next, let's work on accessing the repl from the command line. First, we'll want to make a main function, which will be called when the file is run.

```python

def main():
    pass


if __name__ == '__main__':
    main()
```

Now let's flesh that out a little bit. When main is run, we want to launch the repl with a specific Markov chain.
'abcdefghij'
```python
def main():
    m = Markov('abcdefghij')
    repl(m)


if __name__ == '__main__':
    main()
```

When you run this file, you will see that the repl launches. You can run the file by running `python3 markov.py` in a terminal. Play around with it for a bit, and then hit Ctrl-C to exit.

Now, we might also want to be able to pass in data to this script. We can do that with command line parameters. For example, if we called
`python3 markov.py abcdefghij`, we could pass in the data to make the Markov chain with. All those commands will be put into a variable called `sys.argv`, which we can access like this:

```python
import sys

...

if __name__ == '__main__':
    main(sys.argv[1:])
```

Now, let's open up `step2.py` and make our main function actually accept input.