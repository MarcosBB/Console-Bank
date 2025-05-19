from textual.app import App
from textual.binding import Binding
from ..bank import Bank
from . import screens

class FrontendApp(App):
    CSS_PATH = "style.tcss"
    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),
    ]
    MODES = {
        "main": screens.MainScreen,
        "deposito": screens.DepositoScreen,
        "saque": screens.SaqueScreen,
        "transferencia": screens.TransferenciaScreen,
        "login": screens.LoginScreen,
        "cadastro": screens.CadastroScreen,
    }

    def __init__(self, bank) -> None:
        super().__init__()
        self.bank = bank
        self.current_account = 1

    def on_mount(self) -> None:
        self.switch_mode("login")


