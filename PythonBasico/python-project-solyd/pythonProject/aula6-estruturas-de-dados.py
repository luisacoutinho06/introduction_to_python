# Eu tenho uma lista ordenada e mutável:
minha_lista = ['Mônica', 'Magali']

# E eu tenho uma TUPLA ou uma lista não mutável. E eu consigo substituir somente caso seja a tupla toda.
minha_tupla = ('Cascão', 'Cebolinha')

# Temos o dicionário, que contém o valor e a chave, que ficaria:
#                  KEY          VALUE
meu_dicionario = {'nome': 'Bob Esponja'}
# A melhor forma de se criar um dicionário é usando:
dicionario = dict()

# Temos o conjunto que é parecido com uma lista, ele contém valores, mas não consigo colocar itens iguais, como por exemplo: meu_conjunto = {'Patrick', 'Patrick'} e não tem indice.
# Ele não é ordenado. A melhor forma de se criar um conjunto é usando:
conjunto = set()
meu_conjunto = {'Bob Esponja', 'Patrick'}

# Eu consigo criar uma lista com todas as listas que estão acima.
loucura = [(1,2), (3,4), ({'João', 'Maria'}, {'Gabriel'})]

print(loucura)