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

        transitions = results.get(current, {})

        # TODO replace this if statement
        if next not in transitions:
            transitions[next] = 1
        else:
            transitions[next] += 1
        results[current] = transitions

    return results