# Os blocos de código qe tratamento de exceções e de erro, são feitos para que o programa não se quebere e não feche.
# try:
#    a = 1000 / 0
# except ZeroDivisionError:
    # E então nós aprendemos a tratar estes erros dentro do except.
#    print('Divisão por zero é impossível de se fazer')

# except NameError:
#    print('Você digitou algo errado!')

# E podemos também criar um genérico:
# except Exception as ex:
#    print('Aconteceu um erro:', ex)

#print('aaaaaaa')

import time

def abre_arquivo():
    try:
        arquivo = open('arquivodoido.txt')
        return True
    except Exception as ex:
        print('Aconteceu algum erro:', ex)
        return False

while not abre_arquivo():
    print('Tentando abrir o arquivo!')
    time.sleep(5)

print('Consegui abrir o arquivo!')
