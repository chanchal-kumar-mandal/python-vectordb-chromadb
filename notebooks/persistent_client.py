import chromadb
from chromadb.utils import embedding_functions

# Initialize the default embedding function explicitly
default_ef = embedding_functions.DefaultEmbeddingFunction()

# Initialize Chroma Persistent Client with the same local folder path
chroma_client = chromadb.PersistentClient(path="./chroma_db")

# Get collection with the explicit embedding function
collection = chroma_client.get_collection(
    name="my_collection",
    embedding_function=default_ef
)

# Print all stored documents and IDs
print("Retrieved Collection Data:")
print(collection.get())