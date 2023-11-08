import nltk
def tokenize_text(text):
	tokens=nltk.word_tokenize(text)
	return tokens
sample_inputs=["Manoah is a college student.",
		"He loves Music.",
		"His favourite domain is Data Analyst."
		]
for input_text in sample_inputs:
	print("Inputs Text:",input_text)
	tokens=tokenize_text(input_text)
	print("Tokens:",tokens)
	print("---------------")
