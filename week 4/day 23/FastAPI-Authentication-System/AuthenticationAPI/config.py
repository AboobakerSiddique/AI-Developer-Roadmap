import os

from dotenv import load_dotenv


load_dotenv()


# ============================================================
# DATABASE
# ============================================================

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./users.db"
)


# ============================================================
# SECURITY
# ============================================================

SECRET_KEY = os.getenv(
    "SECRET_KEY"
)

JWT_SECRET = os.getenv(
    "JWT_SECRET"
)


# ============================================================
# API KEY
# ============================================================

API_KEY = os.getenv(
    "API_KEY"
)


# ============================================================
# JWT EXPIRATION
# ============================================================

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv(
        "ACCESS_TOKEN_EXPIRE_MINUTES",
        "30"
    )
)


# ============================================================
# REQUIRED SECRETS
# ============================================================

if not SECRET_KEY:
    raise ValueError(
        "SECRET_KEY is not configured"
    )


if not JWT_SECRET:
    raise ValueError(
        "JWT_SECRET is not configured"
    )