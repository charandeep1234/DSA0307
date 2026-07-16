import re

words = input("Enter words: ").split()

for word in words:
    if re.search("ing$", word):
        print(word, "-> Verb")
    elif re.search("ly$", word):
        print(word, "-> Adverb")
    elif re.search("ed$", word):
        print(word, "-> Verb")
    else:
        print(word, "-> Noun")
