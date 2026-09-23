from embedding_utils import get_embedding


text = "FastAPI is a Python web framework."

vector = get_embedding(text)

print("Dimensions:", len(vector))
print("First 10:", vector[:10])
