import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

texts = [
    "Python is a programming language",
    "FastAPI is a Python web framework",
    "Pizza is a popular food"
]

response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=texts
)

for text, embedding in zip(
    texts,
    response.embeddings
):
    print("\nTEXT:")
    print(text)

    print("\nVECTOR DIMENSIONS:")
    print(len(embedding.values))

    print("\nFIRST 10 VALUES:")
    print(embedding.values[:10])
    
import math


def cosine_similarity(a, b):
    dot_product = sum(
        x * y
        for x, y in zip(a, b)
    )

    magnitude_a = math.sqrt(
        sum(x * x for x in a)
    )

    magnitude_b = math.sqrt(
        sum(x * x for x in b)
    )

    return dot_product / (
        magnitude_a * magnitude_b
    )
    
vectors = [
    embedding.values
    for embedding in response.embeddings
]

print("\nSimilarity results:")

print(
    "Python ↔ FastAPI:",
    cosine_similarity(vectors[0], vectors[1])
)

print(
    "Python ↔ Pizza:",
    cosine_similarity(vectors[0], vectors[2])
)

print(
    "FastAPI ↔ Pizza:",
    cosine_similarity(vectors[1], vectors[2])
)