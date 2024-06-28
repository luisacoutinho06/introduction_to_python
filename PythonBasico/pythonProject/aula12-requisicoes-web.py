# Esta é uma biblioteca que realiza requisições.
#import requests
# Esta é uma biblioteca para caso vc queira pegar certas partes das página que é retornada da requisição. Beautiful Soup 4 - pip install bs4

# Eu posso alterar o que eu envio para a requisição.
#cabecalho = {'User-agent': 'Windows 12', 'Referer': 'https://google.com', 'CF_IPcountry': 'US'}

#meus-cookies = {'Ultima-visita': '10-10-2020'}

dados = {'username': 'guigui', 'password': 'guigui123'}

texto = None
#try:
# Existem vários tipos de requisições como: get, post, delete, patch, update e etc.
    #requisicao = requests.get('https://solyd.com.br', headers=cabecalho, cookies= meus-cookies, data=dados)
    #texto = requisicao.text

# Dessa forma conseguimos ver o que contém na resposta retornada.
#    print(requisicao.text)

#except Exception as e:
    #print('Requisição deu erro:', e)

#print(texto)