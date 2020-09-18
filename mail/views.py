from django.views.generic.base import TemplateView


class MailView(TemplateView):
    template_name = 'send_mail.html'
