import requests
from random import choice

# Define the API endpoint
api_endpoint = "https://api.quotable.io/random"

# Send a GET request to the API endpoint
response = requests.get(api_endpoint)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Get a random quote from the response
    quote = data

    # Print the quote
    print(f"{quote['content']} - {quote['author']}")
else:
    # Handle the error
    print("An error occurred while fetching the quote.")