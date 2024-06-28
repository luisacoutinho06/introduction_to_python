'''
EXERCICIO: CRIE UM SOFTWARE DE GERENCIAMENTE BANCÁRIO. ESSE SOFTWARE PODERÁ SER CAPAZ DE CRIAR CLIENTES E CONTAS. CADA CLIENTE POSSUI NOME, CPF, IDADE.
CADA CONTA POSSUI UM CLIENTE, SALDO, LIMITE, SACAR, DEPOSITAR E CONSULTAR SALDO.
'''
from cliente import Cliente
from conta import Conta

cliente1 = Cliente('Luisa Coutinho', '067.716.686-90', 22)
print(cliente1)

conta_da_luisa = Conta(2000, 4000, cliente1)

conta_da_luisa.sacar(250)
print(conta_da_luisa.consultar_saldo())
conta_da_luisa.depositar(2589)
