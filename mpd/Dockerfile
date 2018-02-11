FROM arm32v7/debian:latest
RUN apt-get update && apt-get install mpd -y
COPY ./mpd.conf /etc/mpd.conf
RUN mkdir /mpd
RUN mkdir /mpd/playlists
RUN mkdir /mpd/music
RUN touch /var/lib/mpd/tag_cache && chown -R mpd /var/lib/mpd/tag_cache
RUN mkdir /run/mpd && touch /run/mpd/pid && chown -R mpd /run/mpd/pid
VOLUME ["/mpd/playlists", "/mpd/music"]
EXPOSE 8000 6600
ENTRYPOINT ["mpd", "--stdout", "--no-daemon"]