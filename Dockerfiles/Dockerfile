FROM laiyijie/ubuntu_dev:latest

ADD ./requirements.txt /info/requirements.txt
RUN cd /info/ && pip3 install -r requirements.txt

ADD ./uwsgi_docker.ini /info/uwsgi_docker.ini

RUN mkdir /var/log/django_server/ && mkdir /var/tmp/django_cache/

ADD ./ /django_server

CMD ["./django_server/script/start.sh"]
