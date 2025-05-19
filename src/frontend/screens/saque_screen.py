from textual.widgets import Button, Label, Input
from .base_screen import BaseScreen
from textual.containers import Vertical, Horizontal

class SaqueScreen(BaseScreen):
    def content(self):
        yield Vertical(
            Label("💸 Saque", id="titulo"),
            Input(placeholder="Valor", id="valor"),
            Horizontal(
                Button("Sacar", id="sacar"),
                Button("Voltar", id="voltar"),
                id="botoes"
            ),
            id="container_principal"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "sacar":
            try:
                valor = float(self.query_one("#valor").value)
                result = self.app.bank.debitar(self.app.current_account, valor)
            except ValueError:
                self.notify("Valor inválido!", severity="error", timeout=10)
                result = False

            if result:
                self.app.switch_mode("main")
                self.notify("Saque realizado com sucesso!", severity="success", timeout=10)
            else:
                self.notify("Saldo insuficiente ou valor inválido!", severity="error", timeout=10)
        elif event.button.id == "voltar":
            self.app.switch_mode("main")
