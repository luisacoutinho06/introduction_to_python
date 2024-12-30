class Conta():
    def __int__(self, saldo, limite, cliente):
        self.saldo = saldo
        self.limite = limite
        self.cliente = cliente

    def sacar(self, valor_a_ser_sacado):
        if valor_a_ser_sacado > self.saldo:
            return print('Você não possui este valor em conta para ser sacado!')
        elif valor_a_ser_sacado == 0:
            return print('Sua conta está zerada!')
        return self.saldo - valor_a_ser_sacado

    def depositar(self, valor_a_ser_depositado):
        if valor_a_ser_depositado == 0:
            return print('Não tem como depositar o valor:', valor_a_ser_depositado, 'pois ele está zerado')
        elif valor_a_ser_depositado < 0:
            return print('Não tem como depositar o valor:', valor_a_ser_depositado, 'pois ele é um valor negativo')
        return self.saldo + valor_a_ser_depositado

    def consultar_saldo(self):
        return print('Este é o valor do seu saldo: ', self.saldo)

