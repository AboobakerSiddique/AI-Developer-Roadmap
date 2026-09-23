import chromadb


client = chromadb.PersistentClient(
    path="./chroma_db"
)
collection = client.get_or_create_collection(
    name="documents"
)
collection.add(
    ids=["chunk_001"],
    documents=[
        "FastAPI is a Python web framework."
    ],
    embeddings=[
        [0.1, 0.2, 0.3, 0.4]
    ],
    metadatas=[
        {
            "source": "example.txt",
            "page": 1
        }
    ]
)
result = collection.get(
    ids=["chunk_001"]
)

print(result)