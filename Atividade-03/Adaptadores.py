# Biblioteca
from Interfaces import Notifier_Interface
from Classes import Push
from Classes import SMS

# Adaptador - Notificador -> SMS
class SMS_Adapter(Notifier_Interface):
    def __init__(self, sms: SMS) -> None:
        self.sms = sms

    def send_message(self, message: str, recipent: str) -> bool:
        return self.sms.send_sms(message, recipent)

# Adaptador - Notificador -> Push
class Push_Adapter(Notifier_Interface):
    def __init__(self, push: Push) -> None:
        self.push = push

    def send_message(self, message: str, recipent: str) -> bool:
        return self.push.send_push(message, recipent)
