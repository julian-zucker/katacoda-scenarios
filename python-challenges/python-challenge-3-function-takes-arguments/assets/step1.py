def repl(m):
    print("Welcome to the REPL!")
    print("Hit Ctrl-C to exit.")

    while True:
        txt = input("> ")

        # TODO add a try/except block to handle IndexErrors from this line
        prediction = m.predict(txt)
        print(prediction)