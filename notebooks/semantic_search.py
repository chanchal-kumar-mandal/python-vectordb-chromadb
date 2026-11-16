import chromadb
from chromadb.utils import embedding_functions

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

# Add compact, keyword-dense documents tailored for semantic search
collection.upsert(
    ids=["id1", "id2", "id3", "id4"],
    documents=[
        "Pineapple: tropical, juicy, sweet-tart fruit rich in vitamin C and bromelain.",
        "Apple: crisp, crunchy temperate orchard fruit used in pies and ciders.",
        "Mango: sweet, rich golden-orange tropical stone fruit harvested in summer.",
        "Orange: vibrant citrus fruit packed with vitamin C and citric acid for juices."
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


# ==========================================
# SEMANTIC SEARCH QUERY EXAMPLE
# ==========================================
print("\n--- Running Semantic Search ---")
query_text = "What fruits grow best in warm tropical weather?"

results = collection.query(
    query_texts=[query_text],
    n_results=2  # Return top 2 most semantically relevant matches
)

print(f"Query: '{query_text}'\n")
for q_id, q_doc, q_dist in zip(results["ids"][0], results["documents"][0], results["distances"][0]):
    print(f"Matched ID: {q_id} (Distance: {q_dist:.4f})")
    print(f"Document: {q_doc}\n")