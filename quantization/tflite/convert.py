import os
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2 as Net
import tensorflow as tf
from tensorflow.python.framework import graph_io
from tensorflow.keras.models import load_model
import tensorflow.contrib.tensorrt as trt

save_pb_dir = './models'
model_fname = './models/model.tflite'

model = Net(weights='imagenet')

# Convert the model.
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the model.
with open(model_fname, 'wb') as f:
  f.write(tflite_model)
