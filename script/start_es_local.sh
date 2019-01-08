#!/bin/bash
set -x 
set -e
SCRIPT_PATH=$(dirname $0)
CURRENT_PATH=$(pwd)
CURRENT_TIME=$(date +%Y%m%d_%H%M%S)
cd $SCRIPT_PATH
container_name=dec_es_local
cd ..
if [ false != $(docker inspect -f '{{.State.Running}}' $container_name) ]
then
    docker kill $container_name
    docker rm $container_name
fi
docker pull laiyijie/es_no_auth
docker run \
	-e "bootstrap.memory_lock=true" \
        -e "ES_JAVA_OPTS=-Xms1g -Xmx1g" \
	--ulimit nofile=65536:65536 \
	--ulimit memlock=-1:-1 \
	-v /data/es:/usr/share/elasticsearch/data \
	-v /tmp/es_logs:/usr/share/elasticsearch/logs \
    --network=host -d --name $container_name laiyijie/es_no_auth
