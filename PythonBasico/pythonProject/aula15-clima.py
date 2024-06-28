import requests
import json

cidade = input("Escreva sua cidade: ")

requisicao = requests.get('http://api.openwathermap.org/data/2.5/weather?q=' + cidade + '&appid=')

tempo = json.loads(requisicao.text)

print('Condição do tempo:', tempo['weather'][0]['main'])
print('Condição do tempo:', float(tempo['main']['temp']) - 273.15)
