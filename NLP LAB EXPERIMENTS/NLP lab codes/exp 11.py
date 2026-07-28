from nltk import CFG
from nltk.parse import RecursiveDescentParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'John' | 'Mary'
VP -> V NP
V -> 'likes' | 'sees'
""")

parser = RecursiveDescentParser(grammar)

sentence = input("Enter the sentence: ").split()

print("\nParse Tree:")

for tree in parser.parse(sentence):
    print(tree)
