"""
EXERCICIO: ESCREVA UMA FUNÇÃO QUE RECEBE UM OBJETO DE COLEÇÃO E RETORNA O VALOR DO MAIOR NUMERO DENTRO DESSA COLEÇÃO E DEPOIS
FAÇA OUTRA FUNÇÃO QUE RETORNA O MENOR NUMERO DESSA COLEÇÃO
"""

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def maior(colecaoDeItens):
    maior_numero = colecaoDeItens[0]
    for item in colecaoDeItens:
        if item > maior_numero:
            maior_numero = item

    return maior_numero

def menor(colecaoDeItens):
    menor_numero = colecaoDeItens[0]
    for item in colecaoDeItens:
        if item < menor_numero:
            menor_numero = item

    return menor_numero

print(maior(lista_de_numeros))
print(menor(lista_de_numeros))