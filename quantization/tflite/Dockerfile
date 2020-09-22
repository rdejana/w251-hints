FROM ubuntu:latest

RUN apt update
RUN apt install -y python3-dev python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install testresources setuptools
RUN pip3 install Pillow numpy
RUN pip3 install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp38-cp38-linux_aarch64.whl
WORKDIR /root
RUN mkdir models && mkdir images
COPY models/ ./models/
COPY images/ ./images/

COPY *.py ./
