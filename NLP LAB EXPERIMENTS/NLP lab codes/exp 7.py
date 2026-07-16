import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = input("Enter a sentence: ")

words = nltk.word_tokenize(text)
tags = nltk.pos_tag(words)

print(tags)
