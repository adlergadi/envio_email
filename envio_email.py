# SMTP

import smtplib
import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

from config import (
    email_remetente,
    senha_app,
    email_destinatario,
    email_copia,
    email_copia_oculta,
    assunto,
)

def enviar_email_anexo():
    msg = MIMEMultipart()

    msg['Subject'] = assunto
    msg['From'] = email_remetente
    msg['To'] = email_destinatario
    msg['Cc'] = email_copia
    msg['Bcc'] = email_copia_oculta
    
    corpo_email = f'''
        <p>Boa tarde,</p>
        <p>Testando envio de email com anexos</p>
        <P>Att, Adler</P>
        '''

    msg.attach(MIMEText(corpo_email, 'html'))

    pasta_anexos = "anexos"

    if not os.path.exists(pasta_anexos):
        print("A pasta Anexos não foi encontrada.")
        return

    list_anexos = os.listdir('Anexos')
    
    for anexo in list_anexos:
        caminho_arquivo = os.path.join(pasta_anexos, anexo)

        if os.path.isfile(caminho_arquivo):
            with open(caminho_arquivo, "rb") as arquivo:
                arquivo_anexo = MIMEApplication(arquivo.read(), Name=anexo)

            arquivo_anexo.add_header(
                "Content-Disposition",
                "attachment",
                filename=anexo,
            )

            msg.attach(arquivo_anexo)

    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(msg['From'], senha_app)
    servidor.send_message(msg)
    servidor.quit()

    print('E-mail enviado com sucesso.')

if __name__ == "__main__":
    enviar_email_anexo()