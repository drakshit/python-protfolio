import smtplib, ssl
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()
    username = 'debasish.for.u@gmail.com'
    password = os.getenv("MAIL_PASSWORD")
    receiver = 'jobs.debasish@gmail.com'
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

if __name__ == "__main__":
    send_email('jobs.debasish@gmail.com', """\n Hello Debasish, \n How are you?""")