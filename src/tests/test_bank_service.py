from unittest import TestCase
from src.services import BankService
from src.models import Bank, Account, BonusAccount, SavingsAccount

class TestBankService(TestCase):

    def setUp(self):
        self.bank = Bank()
        self.service = BankService(self.bank)
        self.numero_conta = "12345"

    # Cadastrar conta
    def test_cadastrar_conta_bonus(self):
        result = self.service.cadastrar_conta("bonus", self.numero_conta, {})
        self.assertTrue(result["sucesso"])
        self.assertEqual(result["numero"], self.numero_conta)
        self.assertEqual(self.bank.consultar_tipo_conta(self.numero_conta), "bonus")

    def test_cadastrar_conta_poupanca(self):
        result = self.service.cadastrar_conta("poupanca", self.numero_conta, {"saldo_inicial": 200})
        self.assertTrue(result["sucesso"])
        self.assertEqual(result["numero"], self.numero_conta)
        self.assertEqual(self.bank.consultar_tipo_conta(self.numero_conta), "poupanca")

    def test_cadastrar_conta_simples(self):
        result = self.service.cadastrar_conta("simples", self.numero_conta, {})
        self.assertTrue(result["sucesso"])
        self.assertEqual(result["numero"], self.numero_conta)
        self.assertEqual(self.bank.consultar_tipo_conta(self.numero_conta), "simples")

    def test_cadastrar_conta_tipo_invalido(self):
        result = self.service.cadastrar_conta("corrente", "000", {})
        self.assertIn("erro", result)
        self.assertEqual(result["erro"], "Tipo inválido")

    def test_cadastrar_conta_existente(self):
        self.service.cadastrar_conta("bonus", self.numero_conta, {})
        result = self.service.cadastrar_conta("bonus", self.numero_conta, {})
        self.assertIn("erro", result)
        self.assertEqual(result["erro"], "Conta já existe")

    # Consultar conta
    def test_consultar_conta(self):
        self.service.cadastrar_conta("bonus", self.numero_conta, {})
        dados = self.service.consultar_conta(self.numero_conta)
        self.assertEqual(dados["numero"], self.numero_conta)
        self.assertEqual(dados["tipo"], "Bonus")
        self.assertEqual(dados["saldo"], 0)

    def test_consultar_conta_inexistente(self):
        self.service.cadastrar_conta("bonus", self.numero_conta, {})
        dados = self.service.consultar_conta("999")
        self.assertIn("erro", dados)
        self.assertEqual(dados["erro"], "Conta não encontrada")

    def test_consultar_contas(self):
        self.service.cadastrar_conta("bonus", "1", {})
        self.service.cadastrar_conta("poupanca", "2", {"saldo_inicial": 200})
        contas = self.service.consultar_contas()
        self.assertEqual(len(contas), 2)
        tipos = {c["tipo"] for c in contas}
        self.assertIn("Bonus", tipos)
        self.assertIn("Poupanca", tipos)

    # Consultar saldo
    def test_consultar_saldo(self):
        self.service.cadastrar_conta("poupanca", self.numero_conta, {"saldo_inicial": 500})
        saldo = self.service.consultar_saldo(self.numero_conta)
        self.assertEqual(saldo["saldo"], 500)

    def test_consultar_saldo_inexistente(self):
        saldo = self.service.consultar_saldo("404")
        self.assertIn("erro", saldo)
        self.assertEqual(saldo["erro"], "Conta não encontrada")

    # Creditar
    def test_creditar(self):
        self.service.cadastrar_conta("simples", self.numero_conta, {})
        result = self.service.creditar(self.numero_conta, 100)
        self.assertNotIn("erro", result)
        self.assertEqual(self.bank.contas[self.numero_conta].saldo, 100)
    
    def test_creditar_valor_negativo(self):
        self.service.cadastrar_conta("simples", self.numero_conta, {})
        result = self.service.creditar(self.numero_conta, -50)
        self.assertIn("erro", result)
        self.assertEqual(self.bank.contas[self.numero_conta].saldo, 0)

    def test_creditar_conta_bonus(self):
        self.service.cadastrar_conta("bonus", self.numero_conta, {})
        result = self.service.creditar(self.numero_conta, 200)
        self.assertTrue(result["sucesso"])
        self.assertEqual(self.bank.contas[self.numero_conta].saldo, 200)
        self.assertEqual(self.bank.contas[self.numero_conta].pontos, 10 + 2)

    # Debitar
    def test_debitar(self):
        self.service.cadastrar_conta("poupanca", self.numero_conta, {"saldo_inicial": 200})
        result = self.service.debitar(self.numero_conta, 150)
        self.assertTrue(result)
        self.assertEqual(self.bank.contas[self.numero_conta].saldo, 50)

    def test_debitar_saldo_insuficiente(self):
        self.service.cadastrar_conta("poupanca", self.numero_conta, {})
        result = self.service.debitar(self.numero_conta, 50)
        self.assertIn("erro", result)

    def test_debitar_valor_negativo(self):
        self.service.cadastrar_conta("simples", self.numero_conta, {})
        result = self.service.debitar(self.numero_conta, -50)
        self.assertIn("erro", result)

    # Transferir
    def test_transferir(self):
        self.service.cadastrar_conta("simples", "a", {})
        self.service.cadastrar_conta("simples", "b", {})
        self.service.creditar("a", 300)
        result = self.service.transferir("a", "b", 100)
        self.assertEqual(self.bank.contas["a"].saldo, 200)
        self.assertEqual(self.bank.contas["b"].saldo, 100)

    def test_transferir_saldo_insuficiente(self):
        self.service.cadastrar_conta("poupanca", "x", {})
        self.service.cadastrar_conta("poupanca", "y", {})
        result = self.service.transferir("x", "y", 50)
        self.assertIn("erro", result)

    def test_transferir_conta_checkar_bonificacao(self):
        self.service.cadastrar_conta("bonus", "a", {})
        self.service.cadastrar_conta("bonus", "b", {})
        self.service.creditar("a", 300)
        result = self.service.transferir("a", "b", 100)
        self.assertEqual(self.bank.contas["b"].pontos, 10 + 1)

    # Render juros
    def test_render_juros(self):
        self.service.cadastrar_conta("poupanca", "1", {"saldo_inicial": 1000})
        self.service.cadastrar_conta("poupanca", "2", {"saldo_inicial": 2000})
        self.service.cadastrar_conta("simples", "3", {"saldo_inicial": 1000})

        result = self.service.render_juros(0.1)
        self.assertEqual(result["contas_renderizadas"], 2)
        self.assertEqual(self.bank.contas["1"].saldo, 1001)
        self.assertEqual(self.bank.contas["2"].saldo, 2002)