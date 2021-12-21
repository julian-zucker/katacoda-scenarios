We're going to add functionality to download whole books from the Gutenberg Project, save their text to a file, and build Markov chains from a file. 
With the function from step1, we can download a book from Project Gutenberg, like Frankenstein. Let's download that book.

```python
FRANKENSTEIN_URL = "https://www.gutenberg.org/files/84/84-0.txt"
FRANKENSTEIN_FILE_NAME = 'frankenstein.txt'
fetch_url(FRANKENSTEIN_URL, FRANKENSTEIN_FILE_NAME)
```

Now the file should exist, and we can write code to load it and then make a Markov model from it. Let's go over to `step2.py` and fill out that function!
Once you're done, feel free to actually build a Markov chain and try out some predictions.

```python
m = from_file(FRANKENSTEIN_FILE_NAME, 4)
m.predict('Fran')
```

That mostly produces `'k'`, but sometimes produces other letters!