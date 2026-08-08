import requests
import config

BASE_URL = config.BASE_URL


# ----------------------------
# Register
# ----------------------------
def register(username, email, password):

    data = {
        "username": username,
        "email": email,
        "password": password
    }

    response = requests.post(
        f"{BASE_URL}/register",
        json=data
    )

    return response


# ----------------------------
# Login
# ----------------------------
def login(username, password):
    response = requests.post(
        f"{BASE_URL}/login",
        json={
            "username": username,
            "password": password
        }
    )

    return response


# ----------------------------
# Authorization Header
# ----------------------------
def auth_header():

    return {
        "Authorization": f"Bearer {config.TOKEN}"
    }


# ----------------------------
# Get Current User
# ----------------------------
def get_me():

    response = requests.get(
        f"{BASE_URL}/me",
        headers=auth_header()
    )

    return response


# ----------------------------
# Update Profile
# ----------------------------
def update_profile(username, email):

    data = {
        "username": username,
        "email": email
    }

    response = requests.put(
        f"{BASE_URL}/profile",
        json=data,
        headers=auth_header()
    )

    return response


# ----------------------------
# Delete Account
# ----------------------------
def delete_account():

    response = requests.delete(
        f"{BASE_URL}/account",
        headers=auth_header()
    )

    return response