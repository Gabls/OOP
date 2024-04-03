# Biblioteca
from Interfaces import Notifier_Interface

# Classe - Notificador 
class Notifier(Notifier_Interface):
    def __init__(self, sender: str) -> None:
        self.sender = sender

    def send_message(self, recipent: str, message: str) -> bool:
        print(f'\nDe: {self.sender} \nPara: {recipent} \nMensagem: {message} \nE-mail enviado!')
        return True

# Classe - SMS
class SMS:
    def __init__(self, sender: str) -> None:
        self.sender = sender
        
    def send_sms(self, recipent: str, message: str) -> bool:
        print(f'\nDe: {self.sender} \nPara: {recipent} \nMensagem: {message} \nSMS enviado!')
        return True

# Classe - Push
class Push:
    def __init__(self, sender: str) -> None:
        self.sender = sender
        
    def send_push(self, device: str, message: str) -> bool:
        print(f'\nDe: {self.sender} \nPara: {device} \nMensagem: {message} \nPush enviado!')
        return True
