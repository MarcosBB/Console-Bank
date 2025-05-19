from textual.widgets import Button, Label
from textual.containers import VerticalScroll, Horizontal
from .base_screen import BaseScreen

class MainScreen(BaseScreen):
    def content(self):
        self.saldo_label = Label("")
        self.conta_label = Label("")

        yield Label("Menu Principal")
        yield self.saldo_label
        yield self.conta_label
        yield Horizontal(
            Button("Depositar", id="depositar"),
            Button("Sacar", id="sacar"),
            Button("Transferir", id="transferir"),
            Button("Voltar", id="voltar"),
        )

    def on_mount(self):
        self.atualizar_info()

    def atualizar_info(self):
        self.saldo_label.update(f"Saldo: {self.app.bank.consultar_saldo(self.app.current_account)}")
        self.conta_label.update(f"Conta: {self.app.current_account}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "depositar":
                self.app.switch_mode("deposito")
            case "sacar":
                self.app.switch_mode("saque")
            case "transferir":
                self.app.switch_mode("transferencia")
            case "voltar":
                self.app.switch_mode("main")

    def on_show(self):
        self.atualizar_info()
