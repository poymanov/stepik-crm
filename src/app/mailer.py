from flask_mail import Mail
from flask_mail import Message

mail = Mail()


def send_to_user(email, subject, html_content):
    msg = Message()
    msg.add_recipient(email)
    msg.subject = subject
    msg.html = html_content
    mail.send(msg)
