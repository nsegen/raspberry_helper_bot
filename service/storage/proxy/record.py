from django import forms
from django.contrib.admin.options import TabularInline
from django.urls import reverse
from django.utils.html import format_html

from .base_model_admin import BaseModelAdmin
from storage.models import Attachment
from storage.models import Record
from storage.models import Type


class RecordProxy(Record):

    class Meta:
        proxy = True
        verbose_name = 'Record'
        verbose_name_plural = 'Records'


class RecordForm(forms.ModelForm):

    class Meta:
        model = RecordProxy
        fields = [
            'record_type',
            'note',
        ]


class AttachmentInline(TabularInline):
    verbose_name = 'Attachment'
    verbose_name_plural = 'Attachments'

    model = Attachment
    can_delete = True
    fk_name = 'record'
    fields = [
        'file',
    ]
    extra = 0


class RecordModelAdmin(BaseModelAdmin):

    form = RecordForm

    fields = [
        'record_type',
        'uuid',
        'note',
        'created',
    ]

    readonly_fields = [
        'created',
    ]

    list_display = [
        'record_type',
        'uuid',
        'created',
    ]

    search_fields = (
        'record_type',
        'uuid',
    )

    inlines = [
        AttachmentInline,
    ]
