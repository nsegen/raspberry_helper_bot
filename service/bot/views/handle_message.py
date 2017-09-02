from django.http import HttpResponse
from django.conf import settings
import telebot
import logging

logger = logging.getLogger(__name__)

# Create your views here.


def handle_message(request, token):
    logger.debug(token)
    return HttpResponse(token)
