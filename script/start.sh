#!/bin/bash
python3 /django_server/manage.py migrate
python3 /django_server/manage.py collectstatic --noinput
uwsgi /info/uwsgi_docker.ini
