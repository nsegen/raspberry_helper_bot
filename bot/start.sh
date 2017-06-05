#!/bin/bash

sleep 1

pip install -r requirements.txt

chmod 777 attachments
# python bot/bot.py
python -m ComplexHTTPServer 8001