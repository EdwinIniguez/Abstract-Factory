from factory.gui_factory import GUIFactory
from buttons.mac_button import MacButton

class MacFactory(GUIFactory):
    def create_button(self) -> MacButton:
        return MacButton()

    def dark_mode(self):
        return "Modo oscuro habilitado en Mac"