from factory.gui_factory import GUIFactory
from buttons.windows_button import WindowsButton
# Fábricas concretas
class WindowsFactory(GUIFactory):
    def create_button(self) -> WindowsButton:
        return WindowsButton()

    def enable_transparency(self):
        return "Transparencia habilitada en Windows"