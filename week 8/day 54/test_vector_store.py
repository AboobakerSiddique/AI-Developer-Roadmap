from vector_store import VectorStore
from embedding_utils import get_embedding


store = VectorStore()


documents = [
    "Python is a programming language.",
    "FastAPI is a Python web framework.",
    "Pizza is a popular food."
]


ids = [
    "chunk_001",
    "chunk_002",
    "chunk_003"
]


metadatas = [
    {
        "source": "python.txt",
        "page": 1
    },
    {
        "source": "fastapi.txt",
        "page": 1
    },
    {
        "source": "pizza.txt",
        "page": 1
    }
]


embeddings = [
    get_embedding(document)
    for document in documents
]


store.add_documents(
    ids=ids,
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas
)


query = "What Python framework can I use to build APIs?"

query_embedding = get_embedding(query)


results = store.search(
    query_embedding,
    top_k=2
)


print("\nQUERY:")
print(query)

print("\nRESULTS:")
print(results)