This lab focuses on optimzation of Deep Learning models.  There are three parts to this lab, TensorFlow 1.15 and TensorRT, Tensorflow 2 and TensorFlow Lite, and Jetson Inference.

Start the lab the cloning the this repository onto your Jetson NX and then run the command `sudo jetson_clocks --fan`.

Note, depending on your docker configuration, you may need to prefix any docker command with `sudo`.

## Part 1: TensorFlow 1.15 and TensorRT
This part will explore the differences between the Keras API, the lower level TensorFlow API, and finally a TensorFlow model optimized with TensorRT.  Change to the tenorflow1.15 directory and build the docker container
``
docker build -t part1 .
``

## Part 2: Tensorflow 2 and TensorFlow Lite
## Part 3: Jetson Inference
