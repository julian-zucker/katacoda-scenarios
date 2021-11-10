change `main.py` to:
```python
import markov
import sys

BOOK_URLS = {
    "frankenstein": "https://www.gutenberg.org/files/84/84-0.txt",
    "pride_and_prejudice": "https://www.gutenberg.org/files/1342/1342-0.txt",
    "dracula": "https://www.gutenberg.org/files/345/345-0.txt",
    "moby_dick": "https://www.gutenberg.org/files/1342/1342-0.txt",
}


def main(book_name):
    file_name = BOOK_URLS[book_name] + ".txt"
    markov.fetch_url(BOOK_URLS[book_name], file_name)
    m = markov.from_file(file_name, size=4)
    markov.repl(m)

if __name__ == '__main__':
    main(sys.argv[1])
```
