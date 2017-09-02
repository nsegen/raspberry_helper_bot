from django.db import models
from django.utils import timezone


class BaseManager(models.Manager):
    def get_queryset(self):
        qs = super(BaseManager, self).get_queryset()
        return qs


class Base(models.Model):
    objects = BaseManager()

    created = models.DateTimeField(
        verbose_name='Date',
        default=timezone.now
    )

    updated = models.DateTimeField(
        verbose_name='Update',
        default=timezone.now
    )

    class Meta:
        abstract = True
