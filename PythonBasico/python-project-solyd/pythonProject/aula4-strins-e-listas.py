# O Python entrega uma liberdade de quebrar strings, porque ele enxerga ela como caracteres.
frase = 'Oi, tudo bem?'

# Dessa forma abaixo eu estou pegando o primeiro caractere da lista de caracteres. print(frase[0])
# print(frase[0])

# Posso imprimir também de um item até o outro item como:
# print(frase[0:13])

# Dessa forma posso imprimir os caracteres e ir pulando os que eu preciso:
# print(frase[0:13:2])

# Caso eu queira fazer ao contrário, é só realizar o seguinte:
# print(frase[::-1])

# Caso eu queira que todos os itens dentro da string estejam com a letra minuscula
# print(frase.lower())

# Caso eu queria que faça a separação da string de alguma forma e a transforme em lista.
# print(frase.split(','))

# Agora vamos falar de listas, é dessa forma que se escreve:

# E eu posso misturar tipos dentro da lista, de string, bool, int. Todos possiveis.
# lista_nomes = ['João', 'Maria', 'Guilherme', 'Diego']

# Dessa forma iremos adicionar dentro da lista, usamos o .append()
# lista_nomes.append('Fernanda')
# lista_nomes.append('Lorena')

# Dessa forma eu consigo inserir na lista, examente na posição que eu preciso:
# lista_nomes.insert(1 ,'Creosvaldo')

# Podemos fazer dessa forma também:
# lista_nomes[0] = 'Bruna'

# Podemos contar quantos itens temos na lista:
# contador_joao = lista_nomes.count('João')
# print(contador_joao)

# Eu gostaria de contar quantos itens tem na lista e é da seguinte forma e também a quantidade de caracteres em uma variável string:
# print(len(lista_nomes))

# Temos também o pop(), que sempre irá pegar o primeiro da lista.
#  print(lista_nomes.pop())

# E agora iremos remover:
# lista_nomes.remove('João')

# Eu posso limpar a lista
# lista_nomes.clear()

# print(lista_nomes)

# Caso eu queira colocar o item de trás para frente, ele ficará da seguinte forma o código:
# print(lista_nomes[-1])