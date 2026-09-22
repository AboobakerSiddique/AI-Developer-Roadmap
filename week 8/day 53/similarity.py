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


vector_a = [1, 2, 3]
vector_b = [1, 2, 3]
vector_c = [3, 2, 1]

print("A vs B:")
print(cosine_similarity(vector_a, vector_b))

print("\nA vs C:")
print(cosine_similarity(vector_a, vector_c))