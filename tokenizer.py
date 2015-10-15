

def tokenize_autocomplete(phrase, min=2, max=5):
    tokens = []
    for word in phrase.split():
        token = ''
        index = 0
        tokens.append(word)

        for x in word:
            if index > len(phrase)-1 or index > max:
                break
            if index > min:
                tokens.append(token)
            token += x
            index += 1
    return tokens

print tokenize_autocomplete('hello world')
