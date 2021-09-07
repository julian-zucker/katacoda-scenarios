def get_table(txt):
    """This function returns a dictionary such that dictionary[letter][next] is equal to
    the number of times that `letter` came before `next` in the input `txt`.

    >>>get_table('ab')
    {'a': {'b': 1}}
    """
    results = {}
    for i in range(len(txt)):
        current = txt[i]
        try:
            next = txt[i + 1]
        except IndexError:
            break

        if current in results:
            transitions = results[current]
        else:
            transitions = {}

        if next not in transitions:
            # For you to do!
            pass
        else:
            # For you to do!
            pass
        results[current] = transitions

    return results
