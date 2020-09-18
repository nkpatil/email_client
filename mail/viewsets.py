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
        try:
            receivers_list = list(set(mail_data['receivers'].split(',')))
            cc_list = list(set(mail_data['cc'].split(',')))
            bcc_list = list(set(mail_data['bcc'].split(',')))
            subject = mail_data['subject']
            message = mail_data['message']
            if len(receivers_list) == 0 or subject == "" or message == "":
                return Response({'response': "failed"},
                                status=status.HTTP_400_BAD_REQUEST)
            send_email(subject, message, receivers_list,
                       cc=cc_list, bcc=bcc_list)
            # Save the email values
            Mail(receivers=','.join(receivers_list),
                 cc=','.join(cc_list), bcc=','.join(bcc_list),
                 subject=subject,
                 message=message).save()
            return Response(
                {"response": "success"},
                status=status.HTTP_201_CREATED)
        except Exception as err:
            print(str(err))
        return Response({'response': "failed"},
                        status=status.HTTP_400_BAD_REQUEST)
