"""
EXERCICIO:
FAÇA UM PROGRAMA QUE PERGUNTE A IDADE, O PESO E A ALTURA DE UMA PESSOA E DECIDE SE ELA ESTÁ APTA A SER DO EXERCITO.
PARA ENTRAR NOE EXERCITO É PRECISO TER MAIS DE 18 ANOS E PESAR MAIS DE 60 KILOS E MEDIR MAIS OU IGUAL A 1,70 METROS!

"""
print('VAMOS VALIDAR SE VOCÊ É APTO A ENTRAR NO EXÉRCITO!\nPREENCHA O FORMULÁRIO ABAIXO:')

nome = input('Qual o seu nome? ')
idade = input('Quantos anos você tem? ')
peso = input('Qual o seu peso? ')
altura = input('Qual a sua altura? ')

print('DADOS DO FORMULÁRIO - ', nome)
print('Nome: ', nome)
print('Idade: ', idade)
print('Peso: ', peso)
print('Altura: ', altura)
print('')
print('Resultado:')

if int(idade) > 18 and float(peso) > 60 and float(altura) >= 1.70:
    print('Você está apto a entrar no exército!')
else:
    print('Infelizmente, você não está apto a entrar no exército!')