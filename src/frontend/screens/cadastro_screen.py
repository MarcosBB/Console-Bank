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
            try:
                numero_conta = int(self.query("#numero_conta").first().value)
                tipo = self.query("#tipo_conta").first().value
                self.app.bank.criar_conta(numero_conta, tipo)
                self.app.bank.creditar(
                    numero_conta, float(self.query("#saldo_inicial").first().value)
                )
                self.notify(
                    "Conta cadastrada com sucesso!", severity="success", timeout=10
                )
                self.app.switch_mode("login")
            except ValueError:
                self.notify("Número da conta inválido!", severity="error", timeout=10)

        elif event.button.id == "voltar":
            self.app.switch_mode("login")
