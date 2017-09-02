from django.conf.urls import url, include
from .admin import common_admin

urlpatterns = [
    url(r'', include(common_admin.urls)),
]
