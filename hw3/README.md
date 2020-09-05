# HW3 Hints

The instrustions mentions that a base Ubuntu container image is smaller thatn using an Nvidia one, however the Nvidia image can use a GPU accelerated version of OpenCV.  This repo contains two basic examples for getting OpenCV running: one in a simple Ubuntu image and the other in the Nvidia l4t image.  Note, neither image contains any MQTT code or libraries. 

## Building
From your Jetson NX device
- Check out the repository.  `git clone https://github.com/rdejana/w251`
- Change to the directory `w251/hw3`
- Building the Ubuntu container: ` docker build -t hw3:ubuntu -f Dockerfile.ubuntu . `
- Building the Nvidia container: ` docker build -t hw3:nvidia -f Dockerfile.nvidia . `

## Running
These examples as designed to run interactively and require display

- Ubuntu: `docker run -ti --rm --privileged -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix hw3:ubuntu bash`
- Nvidia l4t: `docker run -ti --rm --privileged -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix hw3:nvidia bash`
