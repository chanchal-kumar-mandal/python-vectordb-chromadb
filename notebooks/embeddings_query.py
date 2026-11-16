import math
import chromadb
from chromadb.utils import embedding_functions

# Cosine similarity function for two vectors
def cosine_similarity(v1, v2):
    dot_product = sum(a * b for a, b in zip(v1, v2))
    magnitude_v1 = math.sqrt(sum(a ** 2 for a in v1))
    magnitude_v2 = math.sqrt(sum(b ** 2 for b in v2))
    
    if magnitude_v1 == 0 or magnitude_v2 == 0:
        return 0.0
    return dot_product / (magnitude_v1 * magnitude_v2)

# Initialize the default embedding function explicitly
default_ef = embedding_functions.DefaultEmbeddingFunction()

# Use PersistentClient (Client() does not accept a path argument)
chroma_client = chromadb.PersistentClient(path="./chroma_db")

# Create collection with the explicit embedding function
collection = chroma_client.get_or_create_collection(
    name="my_collection",
    embedding_function=default_ef
)
print("Collection Name:", collection.name)

# Print persistence directory safely using get_settings()
print("Database Storage Path:", chroma_client.get_settings().persist_directory)

# Add documents without metadata
collection.upsert(
    ids=["id1", "id2", "id3", "id4"],
    documents=[
        "This is a document about pineapple",
        "This is a document about apple",
        "This is a document about mango",
        "This is a document about oranges"
    ]
)

print("\nCurrent Data:")
# Explicitly include embeddings so data["embeddings"] is not None
data = collection.get(include=["embeddings", "documents"])

# Loop through IDs, documents, and embeddings together
for i, resdoc, embd in zip(data["ids"], data["documents"], data["embeddings"]):
    print(f"ID: {i} | Doc: {resdoc}")
    # Printing the first 5 dimensions of the embedding vector to keep output clean
    print(f"Embeddings (first 5 dims): {embd[:5]}...\n")

# Update documents 
collection.update(
    ids=["id4"],
    documents=[
        "This is a document about watermelons"
    ]
)

print("\nUpdated Data (Check Embeddings):")
# Explicitly include embeddings so data["embeddings"] is not None
data1 = collection.get(include=["embeddings", "documents"])

# Loop through IDs, documents, and embeddings together
for i, resdoc, embd in zip(data1["ids"], data1["documents"], data1["embeddings"]):
    print(f"ID: {i} | Doc: {resdoc}")
    # Printing the first 5 dimensions of the embedding vector to keep output clean
    print(f"Embeddings (first 5 dims): {embd[:5]}...\n")


# ==========================================
# COMPARE TWO VECTORS USING COSINE SIMILARITY
# ==========================================
# Let's grab the embedding of id1 (pineapple) and id4 (watermelons)
idx1 = data1["ids"].index("id1")
idx4 = data1["ids"].index("id4")

vector_pineapple = data1["embeddings"][idx1]
vector_watermelon = data1["embeddings"][idx4]

similarity = cosine_similarity(vector_pineapple, vector_watermelon)

print(f"Cosine Similarity between 'pineapple' (id1) and 'watermelons' (id4): {similarity:.4f}")