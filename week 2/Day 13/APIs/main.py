import requests
import json

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1",
        timeout=5
    )

    print(response.status_code)
    print('success!')

except requests.exceptions.RequestException as e:
    print("Error:", e)
    response = None

if response:
    data = response.json()
    print("Name:", data.get("name"))
    print("Email:", data.get("email"))
    print("Company name:", data.get("company", {}).get("name"))