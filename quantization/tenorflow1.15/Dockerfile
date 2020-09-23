FROM nvcr.io/nvidia/l4t-tensorflow:r32.4.3-tf1.15-py3

RUN apt-get update && apt-get install -y vim
RUN pip3 install pillow 

WORKDIR /root
COPY *.py ./

RUN mkdir images
COPY images/* images/
RUN chmod 700  *.py
CMD bash
