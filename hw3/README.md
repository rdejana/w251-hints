# HW3 Hints

The instrustions mentions that a base Ubuntu container image is smaller thatn using an Nvidia one, however the Nvidia image can use a GPU accelerated version of OpenCV.  This repo contains two basic examples for getting OpenCV running: one in a simple Ubuntu image and the other in the Nvidia l4t image.  Note, neither image contains any MQTT code or libraries. 

## Building
From your Jetson NX device
- Check out the repository.  `git clone https://github.com/rdejana/w251`
- Change to the directory `w251/hw3`
- Building the Ubuntu container: ` docker build -t hw3:ubuntu -f Dockerfile.ubuntu . `
- Building the Nvidia container: ` docker build -t hw3:nvidia -f Dockerfile.nvidia . `

## Running
These examples as designed to run interactively and require display.  The use of `--rm` when starting the container indicates that the container is to be deleted when stopped.

- To enable container to use X, run the following from a terminal on your Jetson: `xhost +` 
- To run the Ubuntu image: `docker run -ti --rm --privileged -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix hw3:ubuntu bash`
- to run the Nvidia l4t image: `docker run -ti --rm --privileged -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix hw3:nvidia bash`
- Once started you'll have a shell prompt.  You can now run the python file cam.py with the command `python3 cam.py`.  You should now see an image displayed on your UI. Note, cam.py uses video device 0.  If your camera is using a different device, update the line `cap = cv2.VideoCapture(0)`, replacing 0 with the correct value.  When done, press `q` in the image window to quit.

