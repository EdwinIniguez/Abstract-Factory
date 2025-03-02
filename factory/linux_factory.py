from factory.gui_factory import GUIFactory
from buttons.linux_button import LinuxButton

class LinuxFactory(GUIFactory):
    def create_button(self) -> LinuxButton:
        return LinuxButton()