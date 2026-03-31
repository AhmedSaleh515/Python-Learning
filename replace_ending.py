def replace_ending(sentence, old, new):
    if sentence.endswith(old):
        i = len(old)
        newSentence = "{}".format((sentence[:-i])+new)
        return newSentence
    return sentence

print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
