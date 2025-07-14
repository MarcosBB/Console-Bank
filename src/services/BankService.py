from src.models.account import SavingsAccount


class BankService:
    def __init__(self, banco):
        self.banco = banco

    def cadastrar_conta:
        saldo_inicial = dados.get("saldo_inicial", 0)

        if tipo.lower() == "bonus":
            result = self.banco.criar_conta(numero, "bonus")
        elif tipo.lower() == "poupanca":
            result = self.banco.criar_conta(numero, "poupanca", saldo_inicial)
        elif tipo.lower() == "simples":
            result = self.banco.criar_conta(numero, "simples")
        else:
            return {"erro": "Tipo inválido"}

        if result:
            return {"sucesso": True, "numero": numero}
        return {"erro": "Conta já existe"}

    def consultar_conta(self, numero):
        if numero not in self.banco.contas:
            return {"erro": "Conta não encontrada"}

        conta = self.banco.contas[numero]
        tipo = self.banco.consultar_tipo_conta(numero)

        dados = {
            "tipo": tipo.capitalize(),
            "numero": numero,
            "saldo": conta.saldo,
        }

        if tipo == "bonus":
            dados["bonus"] = self.banco.consultar_pontos_bonus(numero)

        return dados

    def consultar_contas(self):
        contas = []
        for numero, conta in self.banco.contas.items():
            tipo = self.banco.consultar_tipo_conta(numero)
            dados = {
                "numero": numero,
                "tipo": tipo.capitalize(),
                "saldo": conta.saldo,
            }
            if tipo == "bonus":
                dados["bonus"] = self.banco.consultar_pontos_bonus(numero)
            contas.append(dados)
        return contas

    def consultar_saldo(self, numero):
        saldo = self.banco.consultar_saldo(numero)
        if saldo is None:
            return {"erro": "Conta não encontrada"}
        return {"numero": numero, "saldo": saldo}

    def creditar(self, numero, valor):
        result = self.banco.creditar(numero, valor)
        if result:
            return {"sucesso": True, "numero": numero, "valor": valor}
        return {"erro": "Erro ao creditar"}

    def debitar(self, numero, valor):
        result = self.banco.debitar(numero, valor)
        if result:
            return {"sucesso": True, "numero": numero, "valor": valor}
        return {"erro": "Saldo insuficiente"}

    def transferir(self, origem, destino, valor):
        result = self.banco.transferencia(origem, destino, valor)
        if result:
            return {
                "sucesso": True,
                "origem": origem,
                "destino": destino,
                "valor": valor,
            }
        return {"erro": "Erro na transferência"}

    def render_juros(self, taxa=1.0):
        result = self.banco.render_juros_poupanca(taxa)
        if result:
            contas_renderizadas = sum(
                1
                for conta in self.banco.contas.values()
                if isinstance(conta, SavingsAccount)
            )
            return {"sucesso": True, "contas_renderizadas": contas_renderizadas}
        return {"erro": "Erro ao aplicar rendimento"}
