from textual.widgets import Button, Label, Input
from textual.containers import Vertical, Horizontal
from .base_screen import BaseScreen

class RenderJurosScreen(BaseScreen):
    def content(self):
        yield Vertical(
            Label("📥 Render Juros", id="titulo"),
            Input(placeholder="Taxa de juros(%)", id="taxa"),
            Horizontal(
                Button("Render", id="render"),
                Button("Voltar", id="voltar"),
                id="botoes"
            ),
            id="container_principal"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "render":
            try:
                taxa = float(self.query_one("#taxa").value)
                result = self.app.bank.render_juros_poupanca(taxa)
            except ValueError:
                self.notify("Valor inválido!", severity="error", timeout=10)
                result = False

            if result:
                self.app.switch_mode("main")
                self.notify("Rendimento de juros realizada com sucesso!", severity="success", timeout=10)

            else:
                self.notify("Erro ao realizar rendimento de juros!", severity="error", timeout=10)

        elif event.button.id == "voltar":
            self.app.switch_mode("main")
