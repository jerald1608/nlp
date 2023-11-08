#pywsd is a library whereas wordnet, punkt and averaged_perceptron_tagger are resources in nltk
#!pip install pywsd
#nltk.download('averaged_perceptron_tagger')
#nltk.download('wordnet')
#nltk.download('punkt')
from pywsd.lesk import simple_lesk
sentences = ['I went to the bank to deposit my money','The river bank was full of dead fishes']
# calling the lesk function and printing results for both the sentences
print ("Context-1:", sentences[0])
answer = simple_lesk(sentences[0],'bank')
print ("Sense:", answer)
print ("Definition : ", answer.definition())
print ("Context-2:", sentences[1])
answer = simple_lesk(sentences[1],'bank')
print ("Sense:", answer)
print ("Definition : ", answer.definition())
