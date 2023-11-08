import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer()
sentence = "cars, drawing, played"
words = word_tokenize(sentence)
for word in words:
        print(word,":",ps.stem(word))
