from django.db import models
from django.dispatch.dispatcher import receiver

from .base import Base
import os

from .record import Record


def content_file_name(instance, filename):
    uuid = instance.record.uuid
    record_type = instance.record.record_type.record_type
    attachment_type = instance.record.record_type.name
    return os.path.sep.join([record_type, attachment_type, uuid, filename])


class Attachment(Base):

    file = models.FileField(
        upload_to=content_file_name,
    )

    extension = models.CharField(
        verbose_name='File extension',
        max_length=20,
        null=True,
        default='blob',
    )

    record = models.ForeignKey(
        Record,
        related_name="attachments",
        on_delete=models.CASCADE,
        null=False,
    )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.extension = os.path.splitext(self.file.url)[1][1:]
        return super(Attachment, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.file.url

    class Meta:
        db_table = 'attachment'
        app_label = 'storage'
        verbose_name = 'Attachment'
        verbose_name_plural = 'Attachments'


@receiver(models.signals.post_delete, sender=Attachment)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.file:
        storage = instance.file.storage
        if storage.exists(instance.file.name):
            storage.delete(instance.file.name)
