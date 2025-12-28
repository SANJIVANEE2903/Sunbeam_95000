from sentence_transformers import SentenceTransformer
import numpy as np

# Cosine similarity function
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Load embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Sentences
sentences = [
    "I love football.",
    "Soccer is my favorite sports.",
    "Messi talks spanish."
]

# Generate embeddings
embeddings = embed_model.encode(sentences)

# Print embedding vectors and their lengths
for embed_vect in embeddings:
    print("Len:", len(embed_vect), "-->", embed_vect[:4])

# Compute similarities
print(
    "Sentence 1 & 2 similarity:",
    cosine_similarity(embeddings[0], embeddings[1])
)

print(
    "Sentence 1 & 3 similarity:",
    cosine_similarity(embeddings[0], embeddings[2])
)
