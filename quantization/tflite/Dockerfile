FROM nvcr.io/nvidia/l4t-tensorflow:r32.4.3-tf2.2-py3

RUN apt update
RUN apt install -y python3-dev python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install testresources setuptools
RUN pip3 install Pillow numpy
RUN python3 --version
RUN pip3 install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp36-cp36m-linux_aarch64.whl
RUN pip3 install tensorflow_hub
WORKDIR /root
RUN mkdir models && mkdir images
COPY models/ ./models/
COPY images/ ./images/

COPY *.py ./
RUN chmod -R 700 * 
