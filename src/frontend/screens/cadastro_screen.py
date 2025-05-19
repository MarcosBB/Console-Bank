from .base_screen import BaseScreen
from textual.widgets import Button, Label, Input
from textual.containers import Horizontal


class CadastroScreen(BaseScreen):
    def content(self):
        yield Label("Cadastro de Conta")
        yield Input(placeholder="Número da conta", id="numero_conta")
        yield Horizontal(
            Button("Cadastrar", id="cadastrar"),
            Button("Voltar", id="voltar"),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cadastrar":
            try:
                numero_conta = int(self.query("#numero_conta").first().value)
                self.app.bank.criar_conta(numero_conta)
                self.notify("Conta cadastrada com sucesso!", severity="success", timeout=10)
                self.app.switch_mode("login")
            except ValueError:
                self.notify("Número da conta inválido!", severity="error", timeout=10)
        
        elif event.button.id == "voltar":
            self.app.switch_mode("login")