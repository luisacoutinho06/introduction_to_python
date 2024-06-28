# Criando uma lista de nomes:
# nomes = ['Guilherme', 'Marcelo', 'João', 'Julia', 'Bruna']

# Estruturas de laços, a primeira estrutura que veremos será o FOR, para cada objeto dentro de uma coleção, execute tal funcionalidade.
# Que funciona da mesma forma que o foreach em C#.
# for nome in nomes:
    # print(nome)

# Utilizando a função range, conseguimos numerar os itens dentro da lista, como por exemplo, e posso também especifica onde começar a lista:
# lista_de_numeros = range(5)
# lista_de_numeros = range(0, 100, 2)
# lista_de_numeros = range(5, 10)
# for item in lista_de_numeros:
    # print(item)

# E posso inserir o range direto no for também
# for item in range(0, 100, 2):
# print(item)

# E também podemos utilizar o for junto de uma lista e o range, como:
# for i in range(5):
# print(nomes[i])

# Uma forma de utilizar o range e sempre estar correta a quantidade na coleção, seria dessa forma:
# Estamos usando o lenght para verificar quantos existem dentro da lista e depois inserimos no range.
# for i in range(len(nomes)):
#    print(nomes[i])

# Agora iremos inserir novos itens na lista utilizando o laço de repetição for:
# Para cada item dentro da lista eu adicionei um novo OII, ou seja sem temos 5 itens, eu adicionei 5 OII's diferentes.
# for i in range(len(nomes)):
    # print(nomes[i])
    # nomes.append('OII')

# print(nomes)

# Agora iremos utilizar o laço de repetição em uma string.
# palavra = 'Guilherme Junqueira'

# for letra in palavra:
#   print(letra)

# Outra forma de inserir estruturas de laço é utilizando a palavra chave WHILE
# palavra = 'Luisa Coutinho'

# i = 0
# while i < 10:
#     print('i ainda é menor que 10: ', i)
#     i = i + 1
