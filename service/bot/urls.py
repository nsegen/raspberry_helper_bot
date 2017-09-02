from django.conf.urls import url, include
from .views import handle_message, attachment_action

urlpatterns = [
    url(r'^messages/(?P<token>.+)/', handle_message),
    url(r'^attachment_action/(?P<pk>.+)/', attachment_action, name='attachment_action')
]
