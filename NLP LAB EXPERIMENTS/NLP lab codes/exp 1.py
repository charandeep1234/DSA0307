import re

text = input("Enter text: ")
pattern = input("Enter pattern: ")

if re.search(pattern, text):
    print("Pattern Found")
else:
    print("Pattern Not Found")
