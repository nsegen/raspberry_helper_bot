from django import forms
from django.contrib.admin.options import TabularInline
from django.urls import reverse
from django.utils.html import format_html
from django.urls import reverse
from django.utils.html import format_html

from .base_model_admin import BaseModelAdmin
from storage.models import Attachment
from storage.models import Record
from storage.models import Type
from storage.utils import actions


class RecordProxy(Record):

    def action(self):
        record_type = self.record_type.record_type
        link = '<a href="{}">{}</a>'.format(
            reverse(actions[record_type][0], args=(self.pk,)),
            actions[record_type][1]
        )
        return link

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

    def action(self, obj):
        return format_html(
            '<span>'+obj.action()+'</span>'
        )
    action.boolean = False
    action.short_description = 'Action'
    
    form = RecordForm

    fields = [
        'action',
        'record_type',
        'uuid',
        'note',
        'created',
    ]

    readonly_fields = [
        'uuid',
        'created',
        'action',
    ]

    list_display = [
        'record_type',
        'uuid',
        'created',
        'action',
    ]

    search_fields = (
        'record_type',
        'uuid',
    )

    inlines = [
        AttachmentInline,
    ]
