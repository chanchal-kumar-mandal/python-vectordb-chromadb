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

# Add documents and related metadata (using upsert to avoid duplicate ID errors on re-runs)
collection.upsert(
    ids=["id1", "id2", "id3", "id4"],
    documents=[
        "This is a document about pineapple",
        "This is a document about apple",
        "This is a document about mango",
        "This is a document about oranges"
    ],
    metadatas=[
        {"category": "tropical", "season": "summer"},
        {"category": "temperate", "season": "autumn"},
        {"category": "tropical", "season": "summer"},
        {"category": "citrus", "season": "winter"}
    ]
)

# Query the collection
results = collection.query(
    query_texts=["This is a query document about hawaii"],
    n_results=2
)

print("\nQuery Results:")
print(results)

print("\nCurrent Data:")
data = collection.get()

# Loop through IDs, documents, and metadatas together
for i, resdoc, meta in zip(data["ids"], data["documents"], data["metadatas"]):
    print(f"ID: {i} | Doc: {resdoc} | Metadata: {meta}")


# ==========================================
# METADATA FILTERING EXAMPLES
# ==========================================

# 1. Filter by a single metadata field (e.g., category equals 'tropical')
tropical_category = collection.get(where={"category": "tropical"})
print("\nTropical Category Fruits:")
print(tropical_category)

# 2. Filter by another single field (e.g., season equals 'summer')
summer_season = collection.get(where={"season": "summer"})
print("\nSummer Season Fruits:")
print(summer_season)

# 3. Filter with multiple conditions using explicit $and operator
winter_citrus_fruit = collection.get(
    where={
        "$and": [
            {"category": "citrus"},
            {"season": "winter"}
        ]
    }
)
print("\nWinter Citrus Fruits:")
print(winter_citrus_fruit)