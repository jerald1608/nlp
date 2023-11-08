#n-grams smoothing
from collections import defaultdict

def calculate_ngram_probabilities(corpus):
	ngrams = defaultdict(int)
	context = defaultdict(int)
	
	for sentence in corpus:
		words = sentence.split()
		
		for i in range(len(words) - 2):
			trigram = tuple(words[i:i+3])
			ngrams[trigram] += 1
			context[trigram[:2]] += 1
		print(ngrams)
		print("---------------------------------------------------------")
		print(context)
		probabilities = defaultdict(float)
	
	for trigram, count in ngrams.items():
		context_count = context[trigram[:2]]
		probabilities[trigram] = (count + 1)/(context_count + len(ngrams))
		return probabilities
	
corpus = [
	"I love to code",
	"Python is a popular programming language",
	"Coding is fun",
	"I enjoy coding in Python",
	"I love to dance"
]

trigram_probabilities = calculate_ngram_probabilities(corpus)

for trigram, probability in trigram_probabilities.items():
	print(f"Trigram: {trigram}, Probability: {probability:.4f}")
