class Veiculo:
# Dentro de uma classe, a forma correta de se representar suas propriedades é inserindo dessa forma, utilizando métodos.
# Como por exemplo o método inicial, que é chamado de construtor. Ele constrói o objeto, e é escrito dessa forma:
    def __init__(self, cor, rodas, marca, tanque):
        # Agora eu estou definindo no construtor o valor de cada propriedade.
        self.cor = cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque

    def abastecer(self, litros):
        if self.tanque + litros > 150:
           return print('O veiculo não pode abastecer mais do que 150 litros!')
        else:
            self.tanque += litros

        return self.tanque
