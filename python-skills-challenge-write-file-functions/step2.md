We're going to add functionality to download whole books from the Gutenberg Project, save their text to a file, and build Markov chains from a file. First, we'll have to create a function to download data from a URL to a file.

```python
import urllib.request as req

def fetch_url(url, file_name):
    # open the data at the given URL
    file_in = req.urlopen(url)
    # store the data from the url in this variable
    data = file_in.read()
    # open a file to write binary (wb) to
    file_out = open(file_name, mode='wb')
    # write the data and close the file
    file_out.write(data)
    file_out.close()
```

With that function, we can download a book from Project Gutenberg, like Frankenstein. Let's download that book.

```python
FRANKENSTEIN_URL = "https://www.gutenberg.org/files/84/84-0.txt"
FRANKENSTEIN_FILE_NAME = 'frankenstein.txt'
fetch_url(FRANKENSTEIN_URL, FRANKENSTEIN_FILE_NAME)
```

Now the file should exist, and we can write code to load it and then make a Markov model from it. 

```python
def from_file(file_name, size):
    with open(file_name, encoding='utf8') as file_in:
        return Markov(file_in.read(), size)
```

Now, let's build a Markov chain and try out some predictions.

```python
m = from_file(FRANKENSTEIN_FILE_NAME, 4)
m.predict('Fran')
```

That mostly produces `'k'`, but sometimes produces other letters!