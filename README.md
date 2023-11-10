# Bot para o Zoom - Bot for Zoom.  -  *Em desenvolvimento*

## Introdução -  Introduction.

Este projeto tem como objetivo criar um bot para criar as reuniões no Zoom, automaticamente.

This project aims to create a bot to create meetings on Zoom automatically.

### Descrição - Description.
    - O bot irá criar as reuniões e enviar o link para os e-mails que estarão no excel. Cada excel será considerado uma reunião a ser criada.

    - The bot will create the meetings and send the link to the emails that will be in excel. Each excel will be considered a meeting to be created.

### Excel:
    - O nome do excel será composto com o assunto, hora e data da reunião.

    - The excel name will be composed with the subject, time and date of the meeting.

    -- Exemplo - Example: 
            assunto-do-email_hh-mm_dd-mm-aaaa = Entrevista-para-dev-BackEnd_15-30_17-05-2023

            email-subject_hh-mm_dd-mm-yyyy = Interview-for-dev-BackEnd_15-30_17-05-2023


# Instalação - Installation

1.	Pré-Requisitos - Prerequisites

- Python 3.8.3

2.	Dependências - Dependencies

- logging==0.4.9.6
- python-dotenv==1.0.0
- pywinauto==0.6.8

### Zoom:
    - Version: 5.14.11 (17466)
