from textual.widgets import Button, Label, Input
from .base_screen import BaseScreen
from textual.containers import Horizontal

class LoginScreen(BaseScreen):
    def content(self):
        yield Label("Login")
        yield Input(placeholder="Número da conta", id="numero_conta")
        yield Horizontal(
            Button("Entrar", id="entrar"),
            Button("Cadastrar nova conta", id="cadastrar"),
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