from twitter import Twitter
import time
consumer_key = ''
consumer_secret = ''
token_key = ''
token_secret = ''

twitter = Twitter(consumer_key, consumer_secret, token_key, token_secret)
resp = twitter.tweet('Vamos testar a lib')
print(resp)

# for i in range(1, 100):
#    twitter.tweet('Vamos testar a lib' + str(i))
#    time.sleep(3)

pesquisa = twitter.search('Solyd', 'pt')
#print(tweets)

for resultado in pesquisa:
    print(resultado['text'])
    print(resultado['user']['screen_name'])