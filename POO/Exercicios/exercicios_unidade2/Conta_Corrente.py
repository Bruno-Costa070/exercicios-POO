class ContaCorrente:
    def __init__(self, numero_conta, nome_corretista, saldo_conta=0):
        self.numero = numero_conta
        self.nome = nome_corretista
        self.saldo = saldo_conta

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def deposito(self, novo_valor):
        self.saldo += novo_valor

    def saque(self, novo_valor):
        self.saldo -= novo_valor

bruno = ContaCorrente("48033", "bruno", 0)
bruno.alterarNome("Bruno")
bruno.deposito(800)
print("Dono da Conta:", bruno.nome)
print("Saldo na Conta Corrente:", bruno.saldo)

bruno.saque(154)
print("Dono da Conta:", bruno.nome)
print("Saldo na Conta Corrente:", bruno.saldo)