import sentence_transformers
from sentence_transformers import SentenceTransformer

from sklearn.metrics.pairwise import cosine_similarity
def calculate_bert_similarity(text1, text2):
    # Load the pre-trained BERT model
    model = SentenceTransformer('bert-base-uncased')

    # Encode the texts into BERT embeddings
    embedding1 = model.encode([text1])[0]
    embedding2 = model.encode([text2])[0]

    # Calculate cosine similarity between the embeddings
    similarity = cosine_similarity(embedding1.reshape(1, -1), embedding2.reshape(1, -1))

    return similarity[0][0]

# Example usage
text1 = "I like apples"
text2 = "I love apples"
similarity = calculate_bert_similarity(text1, text2)
print("BERT Similarity:", similarity)
