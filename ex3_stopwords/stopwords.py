import nltk
#nltk.download('stopwords')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
data="Let your faith be bigger than your fears."
stopWords=set(stopwords.words('english'))
words=word_tokenize(data.lower())
wordFiltered=[]
for w in words:
	if w not in stopWords:
		wordFiltered.append(w)
print("Words=",words)
print("Stopwords=",stopWords)
print("Filtered words=",wordFiltered)
