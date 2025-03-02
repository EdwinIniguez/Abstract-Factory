from models.application import Application
from factory.gui_factory import *
from factory.windows_factory import *
from factory.mac_factory import *
from factory.linux_factory import *

# Ejemplo de uso
def get_factory(os_name: str) -> GUIFactory:
    factories = {
        "Windows": WindowsFactory(),
        "Mac": MacFactory(),
        "Linux": LinuxFactory()
    }
    return factories.get(os_name, WindowsFactory())  # Default Windows

if __name__ == "__main__":
    os_name = "Mac"
    factory = get_factory(os_name)
    app = Application(factory)
    print(app.render_ui())
