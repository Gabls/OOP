# Biblioteca
from Interfaces import Notifier_Interface
from Classes import Push
from Classes import SMS

# Adaptador - Notificador -> SMS
class SMS_Adapter(Notifier_Interface):
    def __init__(self, sms: SMS) -> None:
        self.sms = sms

    def send_message(self, recipent: str, message: str) -> bool:
        return self.sms.send_sms(recipent, message)

# Adaptador - Notificador -> Push
class Push_Adapter(Notifier_Interface):
    def __init__(self, push: Push) -> None:
        self.push = push

    def send_message(self, recipent: str, message: str) -> bool:
        return self.push.send_push(recipent, message)
