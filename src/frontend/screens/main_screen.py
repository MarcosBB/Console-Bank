from textual.widgets import Button, Label
from textual.containers import Vertical, Horizontal
from .base_screen import BaseScreen

class MainScreen(BaseScreen):
    def content(self):
        self.saldo_label = Label("", id="saldo")
        self.conta_label = Label("", id="conta")

        yield Vertical(
            Label("💰 Menu Principal", id="titulo"),
            self.saldo_label,
            self.conta_label,
            Horizontal(
                Button("Depositar", id="depositar"),
                Button("Sacar", id="sacar"),
                Button("Transferir", id="transferir"),
                Button("Voltar", id="voltar"),
                id="botoes"
            ),
            id="container_principal"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "depositar":
                self.app.switch_mode("deposito")
            case "sacar":
                self.app.switch_mode("saque")
            case "transferir":
                self.app.switch_mode("transferencia")
            case "voltar":
                self.app.switch_mode("login")

    def on_mount(self) -> None:
        self.saldo_label.update(f"Saldo: {self.app.bank.consultar_saldo(self.app.current_account)}")
        self.conta_label.update(f"Conta: {self.app.current_account}")

    def _on_screen_resume(self):
        self.saldo_label.update(f"Saldo: {self.app.bank.consultar_saldo(self.app.current_account)}")
        self.conta_label.update(f"Conta: {self.app.current_account}")
        return super()._on_screen_resume()
