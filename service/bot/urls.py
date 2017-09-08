from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^messages/(?P<token>.+)/', handle_message),
    url(r'^watch_videos/(?P<pk>.+)/', watch_videos, name='watch_videos'),
    url(r'^listen_audios/(?P<pk>.+)/', listen_audios, name='listen_audios'),
    url(r'^print_files/(?P<pk>.+)/', print_files, name='print_files'),
]
