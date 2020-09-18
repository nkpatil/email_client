from django.db import models


class Mail(models.Model):
    """This stores the email details"""
    receivers = models.TextField(null=False)
    cc = models.TextField(null=True, blank=True)
    bcc = models.TextField(null=True, blank=True)
    subject = models.CharField(max_length=100, null=False)
    message = models.TextField(max_length=500, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
