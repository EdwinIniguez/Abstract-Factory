from abc import ABC, abstractmethod

class BaseButton(ABC):
    @abstractmethod
    def render(self):
        pass