FROM resin/rpi-raspbian:stretch
RUN [ "cross-build-start" ]

RUN set -ex \
	&& apt-get update \
	&& DEBIAN_FRONTEND=noninteractive apt-get install -y \
		mpd \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* ~/.cache \
COPY ./mpd.conf /etc/mpd.conf
RUN mkdir /mpd
RUN mkdir /mpd/playlists
RUN mkdir /mpd/music
RUN touch /var/lib/mpd/tag_cache && chown -R mpd /var/lib/mpd/tag_cache
RUN mkdir /run/mpd && touch /run/mpd/pid && chown -R mpd /run/mpd/pid

RUN [ "cross-build-end" ]

VOLUME ["/mpd/playlists", "/mpd/music"]
EXPOSE 8000 6600
ENTRYPOINT ["mpd", "--stdout", "--no-daemon"]