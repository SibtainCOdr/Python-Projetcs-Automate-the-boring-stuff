spam = ['apples', 'bananas', 'tofu', 'dogs']

def list_thing(words ):
    if len(words) == 1:
        return words[0]
    return '{}, and {}'.format(', '.join(words[:-1]), words[-1])

print(list_thing(spam))


# no Idea hwo this works