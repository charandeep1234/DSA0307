from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "running", "studies", "connected"]

for word in words:
    print(word, "->", ps.stem(word))
