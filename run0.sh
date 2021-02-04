#!/bin/bash

CURRENT_PATH=$(pwd)
IMAGE_NAME="denden047/genre"

docker build -t ${IMAGE_NAME} "$CURRENT_PATH"/docker && \
docker run -it --rm \
    --gpus device=0 \
    -v "$CURRENT_PATH":/workdir \
    -w /workdir \
    ${IMAGE_NAME} \
    /bin/bash
