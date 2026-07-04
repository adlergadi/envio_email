# Envio de Emails com Anexos

## Descrição

Projeto simples de estudo para envio automático de e-mails com anexos usando Python e SMTP.

## Funcionalidades

- Envio de e-mail usando Gmail SMTP.
- Corpo do e-mail em HTML.
- Envio com destinatário principal, cópia e cópia oculta.
- Anexo automático dos arquivos dentro da pasta `Anexos`.

## Tecnologias utilizadas

- Python
- smtplib
- email.mime
- os

## Estrutura do projeto

```text
envio-email/
├── envio_email.py
├── config_exemplo.py
├── README.md
├── .gitignore
└── anexos/