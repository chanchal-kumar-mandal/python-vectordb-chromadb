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

# Add documents (using upsert or add - note: adding duplicate IDs might throw an error if they already exist, so you can use upsert if needed)
collection.add(
    ids=["id1", "id2", "id3", "id4"],
    documents=[
        "This is a document about pineapple",
        "This is a document about apple",
        "This is a document about mango",
        "This is a document about oranges"
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

# Corrected loop syntax, variable names, and string keys ("ids" and "documents")
for i, resdoc in zip(data["ids"], data["documents"]):
    print(f"{i} -> {resdoc}")

# Update documents 
collection.update(
    ids=["id4"],
    documents=[
        "This is a document about watermelons"
    ]
)

print("\nCurrent Updated Data:")
data1 = collection.get()

# Corrected loop syntax, variable names, and string keys ("ids" and "documents")
for i, resdoc in zip(data1["ids"], data1["documents"]):
    print(f"{i} -> {resdoc}")


# Delete documents 
collection.delete(
    ids=["id4"]
)

print("\nCurrent Data After Deletion:")
data2 = collection.get()

# Corrected loop syntax, variable names, and string keys ("ids" and "documents")
for i, resdoc in zip(data2["ids"], data2["documents"]):
    print(f"{i} -> {resdoc}")