
from textual.app import ComposeResult
from textual.widgets import Footer, Header
from abc import abstractmethod
from textual.screen import Screen


class BaseScreen(Screen):
    @abstractmethod
    def content(self):
        pass

    def compose(self) -> ComposeResult:
        yield Header()
        yield from self.content()
        yield Footer()

    def on_mount(self) -> None:
        self.title = "Console Bank"

