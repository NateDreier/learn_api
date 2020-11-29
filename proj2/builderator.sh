#!/usr/bin/env bash
set -o errexit
set -o pipefail
set -o nounset
#for the sake of learning, learn how to automatically incrament version numbers. for now it is manual.
# automatically incriment based on whether it is going to be a major, minor or patch
black api.py

if [[ $(docker ps -a --format "{{.Names}}") == "api" ]]; then
    docker stop api > /dev/null 2>&1
    docker rm api --force > /dev/null 2>&1
fi

for i in $(docker images --format "{{.Repository}}:{{.Tag}}"); do
    if [[ `echo $i | cut -d':' -f1`  == "test_api" ]]; then
        current_version=$(echo $i | cut -d':' -f2) 
        docker rmi $i > /dev/null 2>&1
    fi
done

version=$1
docker build -t test_api:$version . > /dev/null 2>&1
docker run -d -p 5000:5000 --name api test_api:$version > /dev/null 2>&1

sleep 2

./testerator.sh

if [[ $? -eq 0 ]]; then
    echo "w00t"
else
    echo "shit broke yo"
fi
