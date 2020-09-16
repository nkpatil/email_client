from rest_framework import viewsets, status
from rest_framework.response import Response

from mail import serializers, filters
from mail.models import Mail
from mail.lib.notification import send_email


class MailViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Mail.objects.all()
    serializer_class = serializers.MailSerializer
    filterset_class = filters.MailFilters

    def create(self, request, format=None):
        mail_data = request.data
        print(mail_data)
        try:
            receivers = mail_data['receivers']
            cc = mail_data['cc']
            bcc = mail_data['bcc']
            subject = mail_data['subject']
            message = mail_data['message']
            send_email(subject, message, receivers.split(','),
                       cc=cc.split(','), bcc=bcc.split(','))
            # Save the email values
            Mail(receivers=receivers, cc=cc, bcc=bcc, subject=subject,
                 message=message).save()
            return Response(
                {"response": "success"},
                status=status.HTTP_201_CREATED)
        except Exception as err:
            print(str(err))
        return Response({'response': "failed"},
                        status=status.HTTP_400_BAD_REQUEST)
