import datetime as dt
from django.core.management.base import BaseCommand

from mail.lib.notification import send_email
from mail.models import Mail


class Command(BaseCommand):
    help = "Command to send email reports."

    def add_arguments(self, parser):
        parser.add_argument('email_receivers', type=str)
        parser.add_argument('date', type=str, nargs='?', default=None)

    def data_to_html_table(self, mails):
        table = "<table class=\"table_border\">"
        table += "<tr><th style=\"width:50px;\">S.N.</th>\
                <th style=\"width:200px;\">Timestamp</th>"
        for i, mail in enumerate(mails):
            table += "<tr><td>{}</td>\
                <td>{}</td></tr>".format(
                (i + 1),
                mail.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            )
        table += "</table>"
        return table

    def handle(self, *args, **options):
        date = options.get("date")
        email_receivers = options.get("email_receivers").split(',')
        if date is None:
            date = dt.datetime.now().date()

        body_style = "<style type=\"text/css\"> \
         .table_border{ \
            border-collapse: collapse; \
            border:1px solid #3C3D3E; \
          } \
          .table_border tr,.table_border td,.table_border th{ \
            border:1px solid #3C3D3E; padding:2px; \
          } \
          .table_border th{background: #2E537D; color: white;} \
        </style>"

        subject = "Email statistics ({})".format(str(date))
        body_html = body_style
        body_html += "Please find the below email statistics:<br/><br/>"

        mails = Mail.objects.filter(timestamp__date=date).order_by('-timestamp')
        body_html += "<h3>Total Emails sent: {}</h3><br/>".format(mails.count())
        body_html += self.data_to_html_table(mails)

        print("Sending email...")
        send_email(subject, body_html, email_receivers)
