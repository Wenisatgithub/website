FROM caowencomeon/uwsgi:1.0
COPY src        /testbed/src
COPY uwsgi.ini  /testbed/uwsgi.ini
VOLUME /var/log
VOLUME /data
EXPOSE 5000
CMD ["uwsgi", "/testbed/uwsgi.ini"]