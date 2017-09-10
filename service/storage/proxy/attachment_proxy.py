from .base_model_admin import BaseModelAdmin
from storage.models import Attachment


class AttachmentProxy(Attachment):

    class Meta:
        proxy = True
        verbose_name = 'Attachment'
        verbose_name_plural = 'Attachments'


class AttachmentModelAdmin(BaseModelAdmin):

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
        'record',
        'extension',
        'file',
        'created',
    ]

    search_fields = (
        'extension',
        'record__record_type__name',
        'record__uuid'
    )

