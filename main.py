# Código padrão de envio de mensagens automáticas
import smtplib # Para de envio de anexos ou imagens dentro do corpo do email basta pesquisar sobre esta biblioteca
import email.message

def enviar_email():  
    corpo_email = """
    <p>Boa tarde!</p>
    <p>Segue meu email automático</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'remetentegmail.com' # Alterar email
    msg['To'] = 'destinatario@gmail.com' # Alterar email
    password = 'senha' # Gerar nova senha no GMAIL em "senhas de app do google"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()
