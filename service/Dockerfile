# FROM python:3.6
FROM resin/raspberrypi3-python:3.6
RUN mkdir /www
WORKDIR /www
#RUN	apt-get update && apt-get install -y \
#	alsa-base \
#    alsa-utils \
#	&& rm -rf /var/lib/apt/lists/*
ADD ./requirements.txt /www/requirements.txt
RUN pip install -r requirements.txt
