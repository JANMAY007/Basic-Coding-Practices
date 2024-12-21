from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = "jrbhatt18p10@gmail.com"
message["to"] = "jrbhatt18p10@gmail.com"
message["subject"] = "code of sending email"
message.attach(MIMEText("body", "text"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("jrbhatt18p10@gmail.com", "swamiji@1954")
    smtp.send_message(message)
    print("Sent...")
