import requests

url = "https://yahoo-weather5.p.rapidapi.com/weather"

querystring = {"woeid": "455828", "format": "json", "u": "f"}

headers = {
    "X-RapidAPI-Key": "aa745af8ecmsh55a384fb9009c46p12fb52jsn68364b3daeaa",
    "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

info = response.json()

print("Cidade:", info['location']['city'])
print("País:", info['location']['country'])
print("Codigo Único:", info['location']['woeid'])
print("Temperatura:", info['current_observation']['condition']['temperature'])
print("Umidade:", info['current_observation']['atmosphere']['humidity'])