# Keila Sofía Caballero Ramos

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib
import getpass

print("Ingresa los Siguientes Datos")
data = {
    "user": "",
    "pass": ""
}
user = input("Correo Emisor: ")
pasw = getpass.getpass("Contraseña: ")
data["user"] = user
data["pass"] = pasw
email_msg = MIMEMultipart()
# datos correo
email_msg["From"] = data["user"]
correo = input("Correo Receptor: ")
receipents = [correo]
email_msg["To"] = ", ".join(receipents)
email_msg["Subject"] = input("Asunto del Correo: ")
message = input("Mensaje del Correo: ")
email_msg.attach(MIMEText(message, "plain"))
path = input("Archivo a enviar: ")
with open(path, "rb") as arch:
    attach = MIMEApplication(arch.read(), _subtype="jpg",)
attach.add_header("Content-Disposition", "attachment", filename=path)
email_msg.attach(attach)
# create server
server = smtplib.SMTP("smtp.office365.com:587")
server.starttls()
server.login(data["user"], data["pass"])
server.sendmail(email_msg["From"], receipents, email_msg.as_string())
server.quit()
print("successfully sent email to %s:" % (email_msg["To"]))
