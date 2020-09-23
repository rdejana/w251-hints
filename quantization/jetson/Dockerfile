FROM dustynv/jetson-inference:r32.4.3

COPY data/ ./data/

RUN wget --show-progress --progress=bar:force:noscroll --no-check-certificate https://nvidia.box.com/shared/static/maidbjiwkg6bz2bk7drwq7rj8v4whdl9.gz -O Inception-v4.tar.gz
RUN tar xvf Inception-v4.tar.gz -C data/networks
RUN rm Inception-v4.tar.gz

RUN wget --show-progress --progress=bar:force:noscroll --no-check-certificate https://nvidia.box.com/shared/static/at8b1105ww1c5h7p30j5ko8qfnxrs0eg.caffemodel -O bvlc_googlenet.caffemodel

RUN mv bvlc_googlenet.caffemodel data/networks


COPY image-test.py ./
RUN chmod 700 image-test.py

