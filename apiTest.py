import requests
import json

# Define the API endpoint
api_url = "https://jsonplaceholder.typicode.com/posts/1"

# Make the GET request
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Format the JSON response
    formatted_data = json.dumps(data, indent=4)
    print("API Response:")
    print(formatted_data)
else:
    print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")
