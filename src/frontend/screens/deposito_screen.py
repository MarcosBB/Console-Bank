from textual.widgets import Button, Label, Input
from textual.containers import Vertical, Horizontal
from .base_screen import BaseScreen

class DepositoScreen(BaseScreen):
    def content(self):
        yield Vertical(
            Label("📥 Depósito", id="titulo"),
            Input(placeholder="Valor", id="valor"),
            Horizontal(
                Button("Depositar", id="depositar"),
                Button("Voltar", id="voltar"),
                id="botoes"
            ),
            id="container_principal"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "depositar":
            try:
                valor = float(self.query_one("#valor").value)
                result = self.app.bank.creditar(self.app.current_account, valor)
            except ValueError:
                self.notify("Valor inválido!", severity="error", timeout=10)
                result = False

            if result:
                self.app.switch_mode("main")
                self.notify("Depósito realizado com sucesso!", severity="success", timeout=10)
            
            else :
                self.notify("Erro ao realizar depósito!", severity="error", timeout=10)

        elif event.button.id == "voltar":
            self.app.switch_mode("main")
