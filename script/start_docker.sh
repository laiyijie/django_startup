#!/bin/bash
set -x 
set -e
SCRIPT_PATH=$(dirname $0)
CURRENT_PATH=$(pwd)
CURRENT_TIME=$(date +%Y%m%d_%H%M%S)
ENV=$1
CMD=$2
cd ${SCRIPT_PATH}

if [[ -z "$1" ]]
then
    ENV=DEFAULT
fi
container_name=server_${ENV}
image_name=django_server
cd ..
docker build . -f Dockerfiles/Dockerfile --tag ${image_name}
if [[ true = $(docker inspect -f '{{.State.Running}}' ${container_name}) ]]
then
    docker kill ${container_name}
    docker rm ${container_name}
fi
docker run -p 8888:8888 -d -e ENV=$ENV --name ${container_name} -v /tmp/django_server:/var/log/django_server ${image_name} $2
