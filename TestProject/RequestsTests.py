import requests

url = "https://binaryjazz.us/wp-json/genrenator/v1/genre/"
response = requests.get(url)
data = response.json()
print(data)

url = "https://api.weatherbit.io/v2.0/current"
params = {
    "lat": "41.5712239",
    "lon": "1.8250731",
    "key": "6ab88364854d422c81230b38cb9a71af",  # replace with your actual API key
    "include": "minutely"
}
response = requests.get(url, params=params)


data = response.json()

print(data)
