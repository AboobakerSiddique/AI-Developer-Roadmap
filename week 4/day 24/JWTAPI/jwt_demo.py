from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "my_super_secret_key_12345"
ALGORITHM = "HS256"

payload = {
    "sub": "aboobaker",
    "email": "aboobaker@example.com",
    "role": "GOD",
    "exp": datetime.utcnow() + timedelta(minutes=10)
}

token = jwt.encode(
    payload,
    SECRET_KEY,
    algorithm=ALGORITHM
)
print()
print("JWT Token:")
print(token)


decoded = jwt.decode(
    token,
    SECRET_KEY,
    algorithms=[ALGORITHM]
)

print("\nDecoded Payload:")
print(decoded)