# Dessa forma eu abro um arquivo:
# open('arquivo.txt')

# Quando eu coloco o open e passo como argumento a palavra w, é porque eu gostaria de escrever o arquivo.
# open('arquivo.txt', 'w')

# Quando eu coloco o open e passo como argumento a palavra r, é porque eu gostaria de ler o arquivo.
# open('arquivo.txt', 'r')

# Quando eu coloco o open e passo como argumento a palavra r, é porque eu gostaria de ler e escrever o arquivo. Mas primeiro ele lê.
# open('arquivo.txt', 'r+')

# Quando eu coloco o open e passo como argumento a palavra a, é porque eu gostaria de criar aquele arquivo.
# open('arquivo.txt', 'a')

# Quando eu coloco o open e passo como argumento a palavra b, é porque eu gostaria de abrir um arquivo que não é texto, pode ser qualquer um.
# open('arquivo.txt', 'b')

#  arquivo = open('arquivo.txt', 'r')

# Este método é para escrever dentro do arquivo:
# arquivo.write('ALOUUUU')

# Consigo inclusive inserir dentro de arquivos de texto o que eu preciso, como por exemplo:
# for i in range (0, 1000):
#    arquivo.write("aaaaa " + str(i) + "\n")

# Este método é para ler o que está dentro do arquivo.
# print(arquivo.read())

# Caso eu queria ler os bytes de um arquivo binário é necessário fazer apenas isso:
# open('logo.png', 'rb')

# Caso eu queira fechar um arquivo é só realizar isto:
# open('arquivo.txt', 'w')