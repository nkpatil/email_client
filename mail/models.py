from django.db import models


class Mail(models.Model):
    """This stores the email details"""
    receivers = models.TextField()
    cc = models.TextField(null=True, blank=True)
    bcc = models.TextField(null=True, blank=True)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
