# Bibliotecas
from Adaptadores import SMS_Adapter, Push_Adapter
from Classes import Notifier, SMS, Push

# Variaveis
sender = {
    'E-mail': 'gabriel.sousa@gmail.com',
    'Number': '+55 (11) 99878-7456',
    'Device': 'Samsung A14 S',
}
recipent = {
    'E-mail': 'arissa.yumi@gmail.com',
    'Number': '+55 (12) 97344-2589',
    'Device': 'iPhone 15 Pro Max',
}
message = 'Teste de E-mail/ SMS/ Notificção Push\n'

# Envio do E-mail
notifier = Notifier(sender['E-mail'])
notifier.send_message(recipent['E-mail'], message)

# Envio do SMS
sms = SMS(sender['Number'])
notifier = SMS_Adapter(sms)
notifier.send_message(recipent['Number'], message)

# Envio do Push
push = Push(sender['Device'])
notifier = Push_Adapter(push)
notifier.send_message(recipent['Device'], message)
