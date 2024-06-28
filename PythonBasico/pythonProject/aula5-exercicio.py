"""
EXERCICIO:
FAÇA UM PROGRAMA QUE LEIA A QUANTIDADE DE PESSOAS QUE SERÃO CONVIDADAS PARA UMA FESTA. A
PÓS ISSO O PROGRAMA IRÁ PERFUNTAR O NOME DE TODAS AS PESSOAS E COLOCAR NUMA LISTA DE CONVIDADOS.
APÓS ISSO IRÁ IMPRIMIR TODOS OS NOMES DA LISTA.
"""

print('FESTA DE ANIVERSÁRIO!!!!!!!!!')
lista_de_convidados = []
quantidade_de_convidados = 1

while quantidade_de_convidados != 12:
   convidado = input('Escreva o nome do(a) convidado(a): ')
   lista_de_convidados.append(convidado)
   quantidade_de_convidados += 1

print('Os convidados são: ')
numeracao_convidado = 0

for convidado in lista_de_convidados:
    numeracao_convidado += 1
    print('Convidado de número: ', numeracao_convidado, '-', convidado )
