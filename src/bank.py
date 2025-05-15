from src.account import Account


class Bank:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero_conta):
        if numero_conta not in self.contas:
            self.contas[numero_conta] = Account(numero_conta)

    def creditar(self, numero_conta, valor):
        if numero_conta in self.contas and valor >= 0:
            self.contas[numero_conta].saldo += valor
            return True
        return False

    def debitar(self, numero_conta, valor):
        if (
            numero_conta in self.contas
            and valor >= 0
            and self.contas[numero_conta].saldo >= valor
        ):
            self.contas[numero_conta].saldo -= valor
            return True
        return False
