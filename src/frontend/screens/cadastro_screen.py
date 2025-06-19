from .base_screen import BaseScreen
from textual.widgets import Button, Label, Input, Select
from textual.containers import Vertical, Horizontal


class CadastroScreen(BaseScreen):
    OPTIONS = [
        "simples",
        "poupanca",
        "bonus",
    ]

    def content(self):
        yield Vertical(
            Label("📝 Cadastro de Conta", id="titulo"),
            Input(placeholder="Número da conta", id="numero_conta"),
            Input(placeholder="Saldo inicial", id="saldo_inicial", value="0"),
            Select(
                options=[(option, option) for option in self.OPTIONS],
                id="tipo_conta",
                prompt="Selecione o tipo de conta",
            ),
            Horizontal(
                Button("Cadastrar", id="cadastrar"),
                Button("Voltar", id="voltar"),
                id="botoes",
            ),
            id="container_principal",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cadastrar":
            numero_conta = int(self.query("#numero_conta").first().value)
            saldo_inicial_input =self.query("#saldo_inicial").first().value
            saldo_inicial = float(saldo_inicial_input) if saldo_inicial_input else 0.0
            tipo = self.query("#tipo_conta").first().value
            result = self.app.bank.criar_conta(
                numero_conta, 
                tipo, 
                saldo_inicial=saldo_inicial
            )

            if result:
                self.notify("Conta cadastrada com sucesso!", severity="success", timeout=10)
                self.app.switch_mode("login")
            else:
                self.notify("Algum erro ocorreu!", severity="error", timeout=10)

        elif event.button.id == "voltar":
            self.app.switch_mode("login")
