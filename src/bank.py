from src.account import Account, BonusAccount


class Bank:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero_conta, tipo="simples"):
        if numero_conta not in self.contas:
            if tipo == "bonus":
                self.contas[numero_conta] = BonusAccount(numero_conta)
            else:
                self.contas[numero_conta] = Account(numero_conta)

    def creditar(self, numero_conta, valor):
        if numero_conta in self.contas and valor >= 0:
            conta = self.contas[numero_conta]
            conta.saldo += valor
            if isinstance(conta, BonusAccount):
                conta.adicionar_pontos_deposito(valor)
            return True
        return False

    def debitar(self, numero_conta, valor):
        if numero_conta in self.contas and valor >= 0:
            self.contas[numero_conta].saldo -= valor
            return True
        return False

    def transferencia(self, conta_origem, conta_destino, valor):
        if conta_origem not in self.contas or conta_destino not in self.contas:
            return False
        if valor < 0:
            return False

        if self.debitar(conta_origem, valor):
            if self.creditar(conta_destino, valor):
                conta_dest = self.contas[conta_destino]
                if isinstance(conta_dest, BonusAccount):
                    conta_dest.adicionar_pontos_transferencia_recebida(valor)
                return True
            else:
                self.creditar(conta_origem, valor)
        return False

    def consultar_saldo(self, numero_conta):
        if numero_conta in self.contas:
            return self.contas[numero_conta].saldo
        return None
