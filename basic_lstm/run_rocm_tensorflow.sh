#!/bin/sh
IMAGE_NAME="dylan/726-simple-lstm"
SHARED_DIR=$HOME/726
SHARED_DIR_MOUNT_PT=/root/726

# this should be run after generating a docker image from the Dockerfile, i.e `docker build -t $IMAGE_NAME .` 
# forward port for tensorboard.
docker run -it --network=host --device=/dev/kfd --device=/dev/dri --ipc=host --shm-size 16G --group-add video --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -v $SHARED_DIR:$SHARED_DIR_MOUNT_PT -p 6006:6006 $IMAGE_NAME
