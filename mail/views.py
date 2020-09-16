from mail import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.views.generic.base import TemplateView


class MailView(TemplateView):
    template_name = 'send_mail.html'
