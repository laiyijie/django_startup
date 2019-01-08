#!/bin/bash
docker run --name indicator_mongo -v /root/laiyijie/mongo_data:/data/db -d --network=host mongo
