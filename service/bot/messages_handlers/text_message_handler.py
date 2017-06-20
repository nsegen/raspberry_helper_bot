from bot_creator import bot
import logging

logger = logging.getLogger(__name__)


@bot.message_handler(content_types=['text'])
def text_message_handler(message):
    logger.debug(message.from_user.username,)
    if message.from_user.username == 'Val_Shklianik':
        msg = 'Заходи сегодня в 1006б =)'
    elif message.from_user.username == 'nsegen':
        msg = 'working'
    else:
        msg = 'not working'
    bot.send_message(message.chat.id, msg)
