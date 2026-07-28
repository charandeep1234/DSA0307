from nltk import CFG
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'John' | 'Mary'
VP -> V NP
V -> 'likes' | 'sees'
""")

parser = EarleyChartParser(grammar)

sentence = input("Enter the sentence: ").split()

print("\nParse Tree:")

for tree in parser.parse(sentence):
    print(tree)
