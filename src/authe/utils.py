from __future__ import absolute_import, unicode_literals
from django.core.mail import send_mail
from django.conf import settings

# Отправка сообщения с подтверждением на почту
def send_verifiy_link(message, email):
    send_mail('Blog', message, settings.DEFAULT_EMAIL_FROM, [email,])


# Отправка сообщения с сбросом пароля на почту
def send_password_reset_link(message, email):
    send_mail('Blog', message, settings.DEFAULT_EMAIL_FROM, [email,])
