#!/bin/bash
set -x 
set -e
SCRIPT_PATH=$(dirname $0)
CURRENT_PATH=$(pwd)
CURRENT_TIME=$(date +%Y%m%d_%H%M%S)
cd $SCRIPT_PATH
container_name=dec_kibana_local
cd ..
if [ false != $(docker inspect -f '{{.State.Running}}' $container_name) ]
then
    docker kill $container_name
    docker rm $container_name
fi
docker pull laiyijie/kibana_no_auth
docker run \
    -e "ES_JAVA_OPTS=-Xms1g -Xmx1g" \
    --network=host -d --name $container_name laiyijie/kibana_no_auth
