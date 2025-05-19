from textual.widgets import Button, Label, Input
from textual.containers import Vertical, Horizontal
from .base_screen import BaseScreen

class LoginScreen(BaseScreen):
    def content(self):
        yield Vertical(
            Label("🔐 Login", id="titulo"),
            Input(placeholder="Número da conta", id="numero_conta"),
            Horizontal(
                Button("Entrar", id="entrar"),
                Button("Cadastrar nova conta", id="cadastrar"),
                id="botoes"
            ),
            id="container_principal"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "entrar":
            try:
                numero_conta = int(self.query("#numero_conta").first().value)
                self.app.current_account = numero_conta
                self.app.switch_mode("main")
            except ValueError:
                self.notify("Número da conta inválido!", severity="error", timeout=10)
        elif event.button.id == "cadastrar":
            self.app.switch_mode("cadastro")
