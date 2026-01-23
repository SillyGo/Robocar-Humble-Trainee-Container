FROM osrf/ros:humble-desktop

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    ros-humble-rqt \
    ros-humble-rqt-image-view \
    ros-humble-image-tools \
    ros-humble-v4l2-camera \
    v4l-utils \
    mesa-utils \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc

RUN mkdir -p /root/ros2_workspace

COPY exemplos_trainee/ /root/exemplos_trainee/

WORKDIR /root
