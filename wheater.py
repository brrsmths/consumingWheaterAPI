import requests
import datetime

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
print("---------------------------")

current_observation = info['current_observation']
print("Temperatura:", current_observation['condition']['temperature'])
print("Clima:", current_observation['condition']['text'])
print("Umidade:", current_observation['atmosphere']['humidity'])
print("---------------------------")

forecasts = info['forecasts']
for forecast in forecasts:
    print("Dados de Previsão")
    print("Dia:", forecast['day'])
 # datetime.datetime.utcfromtimestamp(unix_timestamp) converte o Unix Timestamp (formato de representação de data e hora que é definido como o número de segundos decorridos desde a meia-noite (UTC) de 1º de janeiro de 1970) em um objeto datetime representando a data e hora correspondentes.
    data_legivel = datetime.datetime.utcfromtimestamp(forecast['date'])
    print("Data:", data_legivel)
    print("Temperature Miníma:", forecast['low'])
    print("Temperatura Máxima:", forecast['high'])
    print("Clima:", forecast['text'])
    print("-------------------------")
