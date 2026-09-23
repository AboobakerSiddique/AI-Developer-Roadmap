import chromadb


class VectorStore:

    def __init__(
        self,
        path="./chroma_db",
        collection_name="documents"
    ):
        self.client = chromadb.PersistentClient(
            path=path
        )

        self.collection = (
            self.client.get_or_create_collection(
                name=collection_name
            )
        )

    def add_documents(
        self,
        ids,
        documents,
        embeddings,
        metadatas
    ):
        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search(
        self,
        query_embedding,
        top_k=3
    ):
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

    def delete(self, ids):
        self.collection.delete(
            ids=ids
        )