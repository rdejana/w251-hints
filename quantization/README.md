This lab focuses on optimzation of Deep Learning models.  There are three parts to this lab, TensorFlow 1.15 and TensorRT, Tensorflow 2 and TensorFlow Lite, and Jetson Inference.

Start the lab the cloning the this repository onto your Jetson NX, change to the quantization
 diretory, and then run the command `sudo jetson_clocks --fan`.

Note, depending on your docker configuration, you may need to prefix any docker command with `sudo`.

If you see any memory errors while running, from another window, run the command `sudo sh flush.sh` from the quantization
diretory.

## Part 1: TensorFlow 1.15 and TensorRT
This part will explore the differences between the Keras API, the lower level TensorFlow API, and finally a TensorFlow model optimized with TensorRT.  
Change to the tenorflow1.15 directory and build the docker container
``
docker build -t part1 .
``
Once the image is built, start it with the command

``
docker run -it --rm --runtime nvidia --network host part1 bash
``
The first script will run is `keras_inference.py`.  This script uses the MobilenetV2 model and performs a simple repeated execution on a single image, images/grace_hopper.jpg.
```
python3 keras_inference.py
```
When complete, you'll see results similar to
```
Predicted: [('n03763968', 'military_uniform', 0.8822736), ('n04350905', 'suit', 0.013280491), ('n04591157', 'Windsor_tie', 0.0061216955)]
average(sec):0.07,fps:13.65
```
Take note of the highest result, in this case `military_uniform` and the score.  Feel free to repeat the test multiple times or to change the image used (see the line 'img_path').

Next, we are going to download the model and convert it and h5 file to pb file and to an TensorRT optimized model.
```
python3 downloadAndConvert.py
```
When complete, run the command `ls -lih models/` and notice the two models, frozen_model.pb and trt_graph.pb.  The trt_graph.pb is our TensorFlowRT model.

We'll now test the models with the ` tf_frozen.inference.py` script.

Run the command `python3 tf_frozen.inference.py`.  This will run the model frozen_model.pb using the lower level TensorFlow API (vs Keras). When complete, you'll see something similar to 
```
Predicted: [('n03763968', 'military_uniform', 0.882273), ('n04350905', 'suit', 0.013280602), ('n04591157', 'Windsor_tie', 0.006121756)]
average(sec):0.02,fps:40.59
```
How do this results compare to the Keras inference?  Feel free to repeat or change the image.

Now edit the file tf_frozen.inference.py, changing the following lines from
```
#trt_graph = get_frozen_graph('./models/trt_graph.pb')
trt_graph = get_frozen_graph('./models/frozen_model.pb')
```
to

```
trt_graph = get_frozen_graph('./models/trt_graph.pb')
#trt_graph = get_frozen_graph('./models/frozen_model.pb')
```
This will now use the TensorRT model.  Run `python3 tf_frozen.inference.py`.  When complete, you'll see output similar to
```
Predicted: [('n03763968', 'military_uniform', 0.88309515), ('n04350905', 'suit', 0.012795044), ('n04591157', 'Windsor_tie', 0.005722298)]
average(sec):0.00,fps:216.24
```
What do you notice?  Again, feel free to repeat or change the image.

Type `exit` to shutdown your container.

## Part 2: Tensorflow 2 and TensorFlow Lite
This part will demonstate TensforFlow Lite, a framework designed for edge devices. 
Change to the tflite directory under quantization and build the docker image:
```
docker build -t tflite .
```
Note this image builds on the Nvida  nvcr.io/nvidia/l4t-tensorflow:r32.4.3-tf2.2-py image and may take some time to download.
Start the container with the command `docker run -it --rm --runtime nvidia --network host tflite bash`.

Now run the script `tf2.py`.  This script uses TensforFlow to classify the grace_hopper.jpg file.  For this example, we'll use the model EfficientNet-B1.
```
python3 tf2.py -m https://tfhub.dev/tensorflow/efficientnet/b1/classification/1 -i images/grace_hopper.jpg -c 20
```

## Part 3: Jetson Inference
