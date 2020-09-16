from django.contrib import admin

from mail.models import Mail


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('receivers', 'subject', 'timestamp')
