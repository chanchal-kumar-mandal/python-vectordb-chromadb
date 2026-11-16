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

# Add documents
collection.add(
    ids=["id1", "id2"],
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges"
    ]
)

# Query the collection
results = collection.query(
    query_texts=["This is a query document about hawaii"],
    n_results=2
)

print(results)