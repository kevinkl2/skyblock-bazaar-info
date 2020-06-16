#!/bin/bash

docker-compose down
docker volume prune
docker rmi skyblock-bazaar-info_web skyblock-bazaar-info_db_updater skyblock-bazaar-info_client