words = input("Enter words: ").split()

for word in words:
    tag = "NOUN"

    if word.endswith("ing"):
        tag = "VERB"
    elif word.endswith("ly"):
        tag = "ADVERB"

    print(word, "->", tag)
