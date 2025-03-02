from buttons.base_button import BaseButton

# Implementaciones concretas para Linux
class LinuxButton(BaseButton):
    def render(self):
        return "Botón estilo Linux"