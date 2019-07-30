#!/bin/bash
set -x 
set -e
SCRIPT_PATH=$(dirname $0)
CURRENT_PATH=$(pwd)
CURRENT_TIME=$(date +%Y%m%d_%H%M%S)
#ENV=$1
#if [ -z $ENV ]; then
#    echo "Please specify  env. Eg. $0 dev"
#    exit 1
#fi
ENV=dev

IMG_NAME=django_start_up

# build docker
cd $SCRIPT_PATH
cd ..

docker build . -f Dockerfiles/Dockerfile --tag ${IMG_NAME}

# kill old docker
container_name=${IMAGE_NAME}_${ENV}_manage
if [ false != $(docker inspect -f '{{.State.Running}}' $container_name) ]
then
    docker kill $container_name
fi
docker rm $container_name || echo "ok"

# Set env variable
ENV_FILE_PATH=./script/env.list.$ENV
ENV_OPTION=
if [ -f $ENV_FILE_PATH ]; then
    ENV_OPTION="--env-file $ENV_FILE_PATH"
else
    echo "No env file ./script/env.list.$ENV not exists"
    exit 1
fi

# Start new docker
docker run -p 8000:8000 -it --rm $ENV_OPTION --name $container_name -v /tmp/${IMG_NAME}:/var/log/dec_server -v $(pwd)/django_server:/django_server ${IMG_NAME} python3 /django_server/manage.py $@
