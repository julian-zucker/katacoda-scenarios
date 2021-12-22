First, we need to cover some topics about handling files and downloading things from the internet.
 
To open a file to read from or to write to, you can use the Python function `open`. Here' an example of writing to a file, and reading from that same file. `open` returns a file descriptor that can be used with the methods `read` and `write`.

```python
with open('file.txt', 'w') as f:
    f.write('foo')

with open('file.txt', 'r') as f:
    print(f.read())
```

To access data on the internet, you can use the library `urllib`. Here's an example of retrieving data at a URL.
```python
import urllib.request as req

file_in = req.urlopen("http://example.com")
data = file_in.read()
print(data)
```

Now that you know how to download data from the internet, let's modify the function `fetch_url` in `step1.py` to download data from the internet.