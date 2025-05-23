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

    def transferencia(self, conta_origem, conta_destino, valor):
        if (conta_origem not in self.contas 
            or conta_destino not in self.contas
            or  valor < 0
        ):
            return False
        
        if self.contas[conta_origem].saldo >= valor:
            if self.debitar(conta_origem, valor):
                if self.creditar(conta_destino, valor):
                    return True
                else:
                    self.creditar(conta_origem, valor)
        return False
    
    def consultar_saldo(self, numero_conta):
        if numero_conta in self.contas:
            return self.contas[numero_conta].saldo
        return None


