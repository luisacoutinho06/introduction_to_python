# Agora irei importar o veiculo:
from veiculo import Veiculo

# Após crarmos a classe iremos fazer com que a classe herde as propriedades da classe pai que é o veiculo. Isto é herança.
class Carro(Veiculo):

# Agora irei fazer o construtor da classe:
    def __init__(self, cor, marca, tanque):
        Veiculo.__init__(self, cor, 4, marca, tanque)

