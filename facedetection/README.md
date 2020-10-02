# FaceDetection




## Using BlazeFace
BlazeFace is a fast, light-weight face detector from Google Research that builds on Single Shot MultiBox Detector (SSD).  This example uses the work done at https://github.com/hollance/BlazeFace-PyTorch to convert from a TFLite model to a PyTorch compatable one.  See https://github.com/hollance/BlazeFace-PyTorch for additional details.

### Installing
Run the following commands to install the required packages on your NX.  For other OS's, you'll need to adjust as needed.  
```
apt-get update
apt-get install python-opencv python3-dev python3-pip
pip3 install torch torchvision numpy pillow
```


### Running
Run the command:
```
python3 dl_cam.py
```
