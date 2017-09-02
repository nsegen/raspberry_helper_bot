from django.contrib.admin.sites import AdminSite
from django.contrib import admin

from .models import Type
from .proxy import *


class ApplicationSite(AdminSite):
    site_header = 'Admin Area'
    site_title = 'Admin Area'
    index_title = 'Admin Area'

    def register(self, model_or_iterable, admin_class=None, **options):
        super(ApplicationSite, self).register(model_or_iterable, admin_class, **options)


admin.site = ApplicationSite(name='Admin Area')

admin.site.register(Type)
admin.site.register(RecordProxy, RecordModelAdmin)
admin.site.register(AttachmentProxy, AttachmentModelAdmin)
