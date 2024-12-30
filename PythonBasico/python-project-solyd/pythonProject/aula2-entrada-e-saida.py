

# PARTE 1 DA AULA 2


# Impressão na tela e caso eu queira pular de linha dentro do próprio print é só fazer isso:
# print('Hello World!\nSegundo print')

# O simbolo /t já siginifca que é para dar um espaçamento referente ao que setamos quando clicamos na tecla tab.
# print('Hello World!\tSegundo print')

# Isto é uma variável e então estou imprimindo o valor da variável na tela. E em python eu posso inserir absolutamente tudo dentro de uma variável.
# Variáveis em python sõa sempre escritas com letras minúsculas e sempre que eu for escrever uma variável maior com duas ou mais palavras,
# sempre concatenar com _
# nome = 'Luisa'
# idade = 22
# altura = 1.56
# tipo_nome = type(nome)
# tipo_idade = type(idade)
# tipo_altura = type(altura)

# print(nome, tipo_nome)
# Quando colocamos a idade dentro do print, e por se tratar de um inteiro. O python meio que já converte automaticamente.
# print(idade, tipo_idade)
# print(altura, tipo_altura)

# Na linha de cima ele está imprimindo na tela o nome na função debaixo ele está mostrando qual o tipo da variável:
#print(type(nome))



# PARTE 2 DA AULA 2



# Hora de refatorar o que fizemos ali encima.
# nome = 'Luisa'
# idade = 22
# altura = 1.56

# print(nome, 'tem', idade, 'anos', 'e possui', altura, 'metros')

# Existem outras formas de concatenar e imprimir na tela, como:
# Porém o python não realiza a conversão de forma implicita, deve ser feito de forma explicita. Então ao fazer o código str() eu estou convertendo aquela
# variável em string. O + não coloca o espaço.
#print(str(nome) + ' tem ' + str(idade) + ' anos ' + 'e possui ' + str(altura) + ' metros.')

# Agora vamos realizar um programa onde ele pergunta quais são os dados do usuário.
# O input é uma função onde caso queiramos, passamos um argumento onde ele recebe os dados que foram digitados no console. E ele sempre irá retornar um
# tipo string, mesmo que a gente passe um número.

# nome = input('Escreva seu nome: ')
# idade = input('Escreva a sua idade: ')
# altura = input('Escreva a sua altura: ')

# print(nome, 'tem', idade, 'anos', 'e possui', altura, 'metros')
# print(type(nome), type(idade), type(altura))



# PARTE 2 DA AULA 2


# Agora iremos realizar um programa de calculadora:
# numero1 = 27
# numero2 = 53
# numero3 = 74.3

# resultado = (numero1 + numero2) / numero3 * 5

# print(resultado)

# Caso eu queira elevar ao quadrado é só realizar este código:
# 10 ** 2

