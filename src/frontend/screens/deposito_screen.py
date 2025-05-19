from textual.widgets import Button, Label, Input
from .base_screen import BaseScreen
from textual.containers import Horizontal

class DepositoScreen(BaseScreen):
    def content(self):
        yield Label("Depósito")
        yield Input(placeholder="Valor", id="valor")
        yield Horizontal(
            Button("Depositar", id="depositar"),
            Button("Voltar", id="voltar"),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "depositar":
            try:
                valor = float(self.query_one(Input).value)
                result = self.app.bank.creditar(self.app.current_account, valor)
            except ValueError:
                self.notify("Valor inválido!", severity="error", timeout=10)
                result = False
            
            if result:
                self.app.switch_mode("main")
                self.notify("Depósito realizado com sucesso!", severity="success", timeout=10)
        
        elif event.button.id == "voltar":
            self.app.switch_mode("main")

