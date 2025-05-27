from src.account import Account, BonusAccount, SavingsAccount


class Bank:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero_conta, tipo="simples"):
        if numero_conta not in self.contas:
            if tipo == "bonus":
                self.contas[numero_conta] = BonusAccount(numero_conta)
                return
            if tipo == "poupanca":
                self.contas[numero_conta] = SavingsAccount(numero_conta)
                return
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
        if (
            numero_conta in self.contas
            and valor >= 0
            and self.contas[numero_conta].saldo - valor
            >= -self.contas[numero_conta].limite
        ):
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

    def render_juros_poupanca(self, taxa_percentual):
        for conta in self.contas.values():
            if isinstance(conta, SavingsAccount):
                try:
                    conta.render_juros(taxa_percentual)
                except Exception as e:
                    return False
        return True

    def consultar_tipo_conta(self, numero_conta):
        if numero_conta in self.contas:
            if isinstance(self.contas[numero_conta], BonusAccount):
                return "bonus"
            if isinstance(self.contas[numero_conta], SavingsAccount):
                return "poupanca"
            return "simples"
        return None

    def consultar_pontos_bonus(self, numero_conta):
        if (
            numero_conta in self.contas
            and self.consultar_tipo_conta(numero_conta) == "bonus"
        ):
            if isinstance(self.contas[numero_conta], BonusAccount):
                return self.contas[numero_conta].pontos
        return None
