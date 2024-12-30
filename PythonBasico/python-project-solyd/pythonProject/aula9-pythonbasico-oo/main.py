# Agora estou importando a classe Veiculo dentro do arquivo.
from veiculo import Veiculo

# Agora vou criar um objeto do tipo Veiculo:
caminhao_rosa = Veiculo('rosa', 8, 'ford', 10)
carro_azul = Veiculo('azul', 4, 'bmw', 30)

# Criamos um objeto do tipo Veiculo:
print(type(caminhao_rosa))

print('CAMINHÃO ROSA')
print('Cor:', caminhao_rosa.cor)
print('Rodas:', caminhao_rosa.rodas)
print('Marca:', caminhao_rosa.marca)
print('Tanque:', caminhao_rosa.tanque)

print('')

print('CARRO AZUL')
print('Cor:', carro_azul.cor)
print('Rodas:', carro_azul.rodas)
print('Marca:', carro_azul.marca)
carro_azul.abastecer(200)
print('Tanque:', carro_azul.tanque)
