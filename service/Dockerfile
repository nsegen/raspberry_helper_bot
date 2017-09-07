FROM python:3.6
# FROM tobi312/rpi-raspberrypi2-python-qemu:3.6
ADD pyipptool.cfg/ /etc/pyipptool/pyipptool.cfg
RUN mkdir /www
WORKDIR /www
ADD ./requirements.txt /www/requirements.txt
RUN pip install -r requirements.txt
