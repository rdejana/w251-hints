# FaceDetection




## Using BlazeFace
BlazeFace is a fast, light-weight face detector from Google Research that builds on Single Shot MultiBox Detector (SSD).  This example uses the work done at https://github.com/hollance/BlazeFace-PyTorch to convert from a TFLite model to a PyTorch compatable one.  See https://github.com/hollance/BlazeFace-PyTorch for additional details.

### Building Docker file
Clone this repository and change into the facedetection directory.  Note, this is assuming your id can invoke docker.  You may need to use sudo.

```
git clone https://github.com/rdejana/w251
cd w251/facedetection
docker build -t facedemo .
```


### Running
Note, all scripts are using the device 0 for the camera and depneding on your configuration, you may need to update.
Start an instance.
```
docker run -ti --rm --privileged -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix facedemo bash
```

There are three Python files to run.
- haarcascade_cam.py: uses openCV's haarcascade
- dl_cam.py: uses BlazeFace-PyTorch
- stereo.py: runs both (not optizmized though...)

Start with haarcascade_cam.py and change your orientation of the camea (move left, right, up, down, rotate etc).  Hows does the face detection work?

Now try with dl_cam.py and repeat your testing.  How do your results change, if they do.

If you like you can try stereo.py.  You'll need to move the two windows so they are side by side (this may 'pause' the execution for a moment or two) and repeat your tests.

```
python3 <script name>
```

Press 'q' to stop while a window is focused to stop the program.
