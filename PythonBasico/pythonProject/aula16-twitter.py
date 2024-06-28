import oauth2
import json
import pprint
import urllib.parse

consumer_key = ''
consumer_secret = ''
token_key = ''
token_secret = ''

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

query = input('Pesquisa: ')
query_codificada = urllib.parse.quote(query, safe='')
requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=pt')

# Decodificando o byte para string.
decodificar = requisicao[1].decode()

# Dessa forma estou transformando o objeto que recebo em json.
objeto = json.loads(decodificar)
tweets = objeto['statuses']

for tweet in tweets:
    pprint.pprint(tweet['user']['screenname'])
    pprint.pprint(tweet['text'])
    print()