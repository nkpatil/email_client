from django.conf import settings
from django.core.mail import EmailMessage


def send_email(subject, body, recievers, cc=[], bcc=[]):
    msg = EmailMessage(subject, body, settings.EMAIL_HOST_USER, recievers)
    if len(cc) > 0:
        msg.cc = cc
    if len(bcc) > 0:
        msg.bcc = bcc
    msg.content_subtype = "html"
    msg.send()
