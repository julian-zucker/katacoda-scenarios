def get_table(txt, size=1):
    """This function returns a dictionary such that dictionary[letter][next] is equal to 
    the number of times that `letter` came before `next` in the input `txt`.

    >>>get_table('ab')
    {'a': {'b': 1}}
    """
    results = {}
    for i in range(len(txt)):
        # change the next line to grab `size` characters using the [...:...] notation
        current = txt[i]
        try:
            # change this line to grab the letter after `current` ends
            next = txt[i+1]
        except IndexError:
            break

        transitions = results.get(current, {})
        transitions.setdefault(next, 0)
        transitions[next] += 1
        results[current] = transitions

    return results

print(get_table('abcdeefdsf', 2))