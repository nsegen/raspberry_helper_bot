from bot_creator import bot
import logging
import requests
import settings
import os
import subprocess
from pathlib import Path


logger = logging.getLogger(__name__)


@bot.message_handler(content_types=['document'])
def document_message_handler(message):
    file_id = message.document.file_id
    file_info = bot.get_file(file_id)
    file = requests.get(
        url='https://api.telegram.org/file/bot{}/{}'.format(
            settings.token, file_info.file_path
        )
    ).content
    Path(message.document.file_name).touch()
    Path(message.document.file_name).write_bytes(file)
    subprocess.run(['lpr', '-P', settings.default_printer, message.document.file_name])
    if message.from_user.username == 'nsegen':
        msg = 'working document'
    else:
        msg = 'not working'
    bot.send_message(message.chat.id, msg)
