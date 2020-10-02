FROM nvcr.io/nvidia/l4t-pytorch:r32.4.3-pth1.6-py3
RUN apt-get update
RUN apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl vim-tiny \
    gnupg-agent \
    vim \
    software-properties-common
RUN apt-key adv --fetch-key https://repo.download.nvidia.com/jetson/jetson-ota-public.asc
## This matches the nx2 and the current jetpack version
RUN add-apt-repository "deb https://repo.download.nvidia.com/jetson/common r32.4 main"
RUN add-apt-repository "deb https://repo.download.nvidia.com/jetson/t194 r32.4 main"

RUN apt-get update
RUN apt install -y nvidia-opencv python3-dev python3-pip
RUN pip3 install Cython  &&  pip3 install numpy

WORKDIR /root
COPY *.xml ./
COPY *.pth ./
COPY *.py ./
COPY *.npy ./
RUN chmod a+rw *
