from django.db import models
from .base import Base


TYPE_BLOB = 'blob'
TYPE_MUSIC = 'music'
TYPE_VIDEO = 'video'
TYPE_DOCUMENT = 'document'
TYPE_PICTURE = 'picture'

TYPES = (
    (TYPE_BLOB, 'BLOB'),
    (TYPE_MUSIC, 'Audio'),
    (TYPE_VIDEO, 'Video'),
    (TYPE_DOCUMENT, 'Document'),
    (TYPE_PICTURE, 'Picture'),
)


class Type(Base):

    record_type = models.CharField(
        verbose_name='Record type',
        max_length=20,
        null=False,
        default=TYPE_BLOB,
        choices=TYPES,
    )

    name = models.TextField(
        verbose_name='name',
    )

    description = models.TextField(
        verbose_name='Description',
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Record Type'
        verbose_name_plural = 'Record Types'