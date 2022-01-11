For this step, we're going to allow users to choose a book to make a Markov chain from.

By running `python3 main.py frankenstein`, they will get a REPL with a Markov chain trained on Frankenstein. By running `python3 main.py dracula`, they can get one trained on Dracula!

In `main.py`, you can see a dictionary mapping from book names to the url with their text. Using the helper function we wrote in the previous sections, which you can find in `markov.py`, download the specified book name, make a Markov chain from its text, and then show the user a `repl` with that chain!
