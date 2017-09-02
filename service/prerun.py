import os
from django.contrib.auth.models import User
from django.conf import settings
import telebot

DEBUG = bool(os.getenv('DJANGO_DEBUG', 'false'))
DJANGO_ADMIN_LOGIN = os.getenv('DJANGO_ADMIN_LOGIN')
DJANGO_ADMIN_MAIL = os.getenv('DJANGO_ADMIN_MAIL')
DJANGO_ADMIN_PASS = os.getenv('DJANGO_ADMIN_PASS')

if DJANGO_ADMIN_LOGIN is not None and \
        not User.objects.filter(username=DJANGO_ADMIN_LOGIN).exists():
    print("[PRERUN] Creating superuser %s/%s (%s)" % (DJANGO_ADMIN_LOGIN, DJANGO_ADMIN_PASS, DJANGO_ADMIN_MAIL))
    User.objects.create_superuser(DJANGO_ADMIN_LOGIN, DJANGO_ADMIN_MAIL, DJANGO_ADMIN_PASS)
else:
    print("[PRERUN] Admin entry exist or not required")

# print('%s/%s/' % (settings.WEBHOOK_URL_BASE, settings.BOT_TOKEN))
# bot = telebot.TeleBot(settings.BOT_TOKEN)
# bot.remove_webhook()
# bot.set_webhook(url='%s/%s/' % (settings.WEBHOOK_URL_BASE, settings.BOT_TOKEN),
#     certificate=open(settings.SSL_CRT, 'rb'))
# print('Set webhook')