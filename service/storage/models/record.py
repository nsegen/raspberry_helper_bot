from django.db import models
from .base import Base
import uuid

from .record_type import Type


def generate_uuid():
    return str(uuid.uuid4())


class Record(Base):

    record_type = models.ForeignKey(
        Type,
        related_name="records",
        on_delete=models.CASCADE,
        null=False,
    )

    uuid = models.TextField(
        blank=False,
        null=False,
        editable=True,
        unique=False,
        verbose_name='UUID',
        default=generate_uuid
    )

    note = models.TextField(
        verbose_name='Note',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.uuid

    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'
