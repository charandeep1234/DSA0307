word = input("Enter a noun: ")

if word.endswith("y"):
    print("Plural:", word[:-1] + "ies")
else:
    print("Plural:", word + "s")
