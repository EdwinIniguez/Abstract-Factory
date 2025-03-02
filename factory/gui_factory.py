from abc import ABC, abstractmethod
from buttons.base_button import BaseButton

# Fábrica abstracta
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> BaseButton:
        pass