pos = {
    "I":"PRON",
    "eat":"VERB",
    "apple":"NOUN",
    "is":"VERB",
    "good":"ADJ"
}

sentence = input("Enter a sentence: ").split()

for word in sentence:
    print(word, ":", pos.get(word, "Unknown"))
