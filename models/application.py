from factory.gui_factory import GUIFactory

class Application:
    def __init__(self, factory: GUIFactory):
        self.button = factory.create_button()
    
    def render_ui(self):
        return self.button.render()