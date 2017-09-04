FROM armhf/python:3.6
ADD pyipptool.cfg/ /etc/pyipptool/pyipptool.cfg
RUN mkdir /www
WORKDIR /www
ADD ./requirements.txt /www/requirements.txt
RUN pip install -r requirements.txt
