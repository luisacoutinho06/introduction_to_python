import re
import request

# regex -> REG = REGULAR E EX = EXPRESSION - Basicamente são máscaras.

# string_de_teste = 'O gato é bonito'
# Estou chamando a biblioteca e agora vou pesquisar dentro de uma string:
# Eu escrevo este r, antes da string para criar uma RAW STRING, ou string crua. Ele pega os caracteres especiais que estão dentro de uma string e retira a funcionalidade deles.
# Para que eu procure uma string genérica, é só inserir o ponto que ele vale qualquer caractere geral:
# E caso eu queira especificar um caractere do tipo palavra, eu utilizo \w
# padrao = re.search(r'ga.', string_de_teste)

# if padrao:
    # Dessa forma vou imprimir o texto que está na variável.
#    print(padrao.group())
#else:
#    print("Padrão não encontrado.")


# Existe uma forma de pesquisar na frase inteira os itens que estão dentro da string.
# string_de_teste = 'O gato, a gata, os gatinhos, os gatões'

# E então é transformado em uma lista.
# Este + traz a palavra por completo, verifica se tem mais letras.
# Com o + eu obrigo a ter uma letra depois do gat, com o asterisco pode ter 0 ou mais.
    # padrao = re.findall(r'gat\w*', string_de_teste)
# Caso eu coloque entre colchetes eu consigo buscar as letras. Caso eu queira uma ou mais letras eu insiro o +
# padrao = re.findall(r'[gat]+', string_de_teste)
# if padrao:
#    print(padrao)
# else:
#    print('Padrão não encontrado')


requisicao = request.get('http://lacoxinha.com.br/contato')
# Agora para criarmos uma expressão regular que consegue pegar o e-mail, é só fazer da seguinte forma:
string_email = 'teste@teste.com, asdajs@adsmao.com, makdmaokmdoasmdoka@amdkamd.com.br, asdamda-akdma@fisica.usp.br, kaodmoas, akdmaokmsl, testeeeee, a@a.cs';
# Primeira coisa que iremos inserir é que sempre terá algo escrito, uma letra e algo a mais.
padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', requisicao)

if padrao:
    print(padrao)
else:
    print('Padrão não encontrado!')
