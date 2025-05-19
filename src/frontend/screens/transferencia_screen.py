from textual.widgets import Button, Label, Input
from textual.containers import Vertical, Horizontal
from .base_screen import BaseScreen

class TransferenciaScreen(BaseScreen):
    def content(self):
        yield Vertical(
            Label("💳 Transferência", id="titulo"),
            Input(placeholder="Conta destino", id="conta_destino"),
            Input(placeholder="Valor", id="valor"),
            Horizontal(
                Button("Transferir", id="transferir"),
                Button("Voltar", id="voltar"),
                id="botoes"
            ),
            id="container_principal"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "transferir":
            try:
                conta_destino = int(self.query("#conta_destino").first().value)
                valor = float(self.query("#valor").first().value)
                result = self.app.bank.transferencia(self.app.current_account, conta_destino, valor)
            except ValueError:
                self.notify("Dados inválidos!", severity="error", timeout=10)
                result = False

            if result:
                self.app.switch_mode("main")
                self.notify("Transferência realizada com sucesso!", severity="success", timeout=10)
            else:
                self.notify("Falha na transferência!", severity="error", timeout=10)
        elif event.button.id == "voltar":
            self.app.switch_mode("main")
