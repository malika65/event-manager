from __future__ import absolute_import, unicode_literals
from django.core.mail import send_mail
from django.conf import settings


from django.core.mail import EmailMessage


import threading


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        EmailThread(email).start()
        
# Отправка сообщения с подтверждением на почту
def send_verified_link(message, email):
    send_mail('Blog', message, settings.DEFAULT_EMAIL_FROM, [email,])


# Отправка сообщения с сбросом пароля на почту
def send_password_reset_link(message, email):
    send_mail('Blog', message, settings.DEFAULT_EMAIL_FROM, [email,])
