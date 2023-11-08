#pos_tags
import nltk
from nltk import word_tokenize
sentence = "I am learning NLP in Python"
tokens = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)
print(pos_tags)

