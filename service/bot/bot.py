from django.conf import settings
import telebot
import logging

logger = logging.getLogger(__name__)
print('%s/%s/' % (settings.WEBHOOK_URL_BASE, settings.BOT_TOKEN))
bot = telebot.TeleBot(settings.BOT_TOKEN)
bot.remove_webhook()
bot.set_webhook(url='%s/%s/' % (settings.WEBHOOK_URL_BASE, settings.BOT_TOKEN),
    certificate=open(settings.SSL_CRT, 'r'))
print('Set webhook')

