import requests

url = "https://api.weatherbit.io/v2.0/current"

params = {
    "lat": "41.5712239",
    "lon": "1.8250731",
    "key": "6ab88364854d422c81230b38cb9a71af",  # replace with your actual API key
    "include": "minutely"
}

response = requests.get(url, params=params)

# Convert the response to JSON format
data = response.json()

# Print the data
print(data)
