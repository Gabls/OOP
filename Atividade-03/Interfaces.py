# Biblioteca
from abc import ABC, abstractmethod

# Interface - Notificador
class Notifier_Interface(ABC):
    @abstractmethod
    def send_message(self, message: str, recipent: str) -> bool:
        pass
