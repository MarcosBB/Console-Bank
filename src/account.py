class Account:
    def __init__(self, numero):
        self.numero = numero
        self.saldo = 0.0

class BonusAccount(Account):
    def __init__(self, numero):
        super().__init__(numero)
        self.pontos = 10

    def adicionar_pontos_deposito(self, valor):
        self.pontos += int(valor // 100)

    def adicionar_pontos_transferencia_recebida(self, valor):
        self.pontos += int(valor // 200)

class SavingsAccount(Account):
    def __init__(self, numero):
        super().__init__(numero)

    def renderJuros(self, taxa_percentual):
        if taxa_percentual < 0:
            raise ValueError("A taxa de juros não pode ser negativa.")
        
        juros = self.saldo * (taxa_percentual / 100)
        self.saldo = juros
