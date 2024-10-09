import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Configurações do e-mail
remetente = "seu_email@gmail.com"
senha = "sua_senha"
destinatario = "croljob@gmail.com"
assunto = "Foto do CFTV"

# Cria o e-mail
msg = MIMEMultipart()
msg["From"] = remetente
msg["To"] = destinatario
msg["Subject"] = assunto

# Corpo do e-mail (opcional)
msg.attach(MIMEText("Segue a foto do CFTV em anexo."))

# Anexa o arquivo
with open(caminho_arquivo_destino, "rb") as arquivo:
    anexo = MIMEApplication(arquivo.read())
    anexo.add_header("Content-Disposition", f"attachment; filename={nome_arquivo}")
    msg.attach(anexo)

# Envia o e-mail
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(remetente, senha)
    server.sendmail(remetente, destinatario, msg.as_string())
    print("E-mail enviado com sucesso!")

# Lembre-se de substituir as informações corretas do seu e-mail.
