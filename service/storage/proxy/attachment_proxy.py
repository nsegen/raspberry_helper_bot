from .base_model_admin import BaseModelAdmin
from storage.models import Attachment
from django.urls import reverse
from django.utils.html import format_html


class AttachmentProxy(Attachment):


    def action(self):
        link = '<a href="{}">{}</a>'.format(reverse('attachment_action', args=(self.pk,)), 'Print file')
        return link
    
    class Meta:
        proxy = True
        verbose_name = 'Attachment'
        verbose_name_plural = 'Attachments'


class AttachmentModelAdmin(BaseModelAdmin):

    def action(self, obj):
        return format_html(
            '<span>'+obj.action()+'</span>'
        )
    action.boolean = False
    action.short_description = 'Action'

    fields = [
        'file',
        'extension',
        'record',
        'created',
    ]

    readonly_fields = [
        'created',
    ]

    list_display = [
        'extension',
        'file',
        'created',
        'action',
    ]

    search_fields = (
        'extension',
    )

