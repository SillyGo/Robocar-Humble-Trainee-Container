#!/bin/bash

mkdir -p "$(pwd)/ros2_workspace"
docker rm ros2-humble-container #necessário, por algum motivo o docker n remove o miseravel

docker run -it \
    --name ros2-humble-container2 \
    --net=host \
    --env DISPLAY=$DISPLAY \
    --env QT_X11_NO_MITSHM=1 \
    --volume /tmp/.X11-unix:/tmp/.X11-unix:rw \
    --volume "$(pwd)/ros2_workspace:/root/ros2_workspace" \
    --device /dev/video0 \
    --group-add video \
    ros2-humble-x11-cam

#este comentário é um easter-egg
