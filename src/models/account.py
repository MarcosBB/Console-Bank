class Account:
    def __init__(self, numero, saldo_inicial=0):
        self.numero = numero
        self.saldo = saldo_inicial
        self.limite = 1000.0



class BonusAccount(Account):
    def __init__(self, numero):
        super().__init__(numero)
        self.pontos = 10

    def adicionar_pontos_deposito(self, valor):
        self.pontos += int(valor // 100)

    def adicionar_pontos_transferencia_recebida(self, valor):
        self.pontos += int(valor // 150)



class SavingsAccount(Account):
    def __init__(self, numero, saldo_inicial):
        super().__init__(numero, saldo_inicial)
        self.limite = 0.0

    def render_juros(self, taxa_percentual):
        if taxa_percentual < 0:
            raise ValueError("A taxa de juros não pode ser negativa.")

        juros = self.saldo * (taxa_percentual / 100)
        self.saldo += juros  # CORREÇÃO: era = agora é +=
