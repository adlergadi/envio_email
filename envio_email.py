# SMTP

import smtplib
import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
from senha_email import senha_app

def enviar_email_anexo():
    msg = MIMEMultipart()
    msg['Subject'] = 'Email enviado com Python'
    msg['From'] = 'adlergadioli@gmail.com'
    msg['To'] = 'atilagadioli@gmail.com'
    # Mandar como copia
    msg['Cc'] = 'adlergadioli+copia@gmail.com'
    # Mandar como copia oculta
    msg['Bcc'] = 'adlergadioli+copia@gmail.com'
    
    # Mandar em formato HTML
    corpo_email = f'''<p>Boa tarde,</p>
    <p>Testando envio de email com anexos</p>
    <P>Att, Adler</P>'''

    msg.attach(MIMEText(corpo_email, 'html'))

    # Anexar arquivos

    list_anexos = os.listdir('Anexos')
    
    for anexo in list_anexos:
        with open(f'Anexos/{anexo}', 'rb') as arquivo:
            msg.attach(MIMEApplication(arquivo.read(), Name=anexo))

    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(msg['From'], senha_app)
    servidor.send_message(msg)
    servidor.quit()
    print('Email enviado')

enviar_email_anexo()