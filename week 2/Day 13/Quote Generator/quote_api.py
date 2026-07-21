import requests


API_URL = "https://dummyjson.com/quotes/random"


def get_random_quote():
    """
    Fetches a random quote from the API.

    Returns:
        tuple: (quote, author)
        Returns (None, None) if an error occurs.
    """

    try:
        response = requests.get(API_URL, timeout=5)

        if response.status_code == 200:
            data = response.json()

            quote = data["quote"]
            author = data["author"]

            return quote, author

        else:
            print(f"Error: Server returned {response.status_code}")
            return None, None

    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
        return None, None