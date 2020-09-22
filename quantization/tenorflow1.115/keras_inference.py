import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2 as Net
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet import preprocess_input, decode_predictions
import numpy as np
import time

#model = Net(weights='imagenet')
model = tf.keras.applications.MobileNet()

img_path = 'images/grace_hopper.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

labels_path = tf.keras.utils.get_file(
    'ImageNetLabels.txt',
    'https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt')
imagenet_labels = np.array(open(labels_path).read().splitlines())


preds = model.predict(x)
# decode the results into a list of tuples (class, description, probability)
# (one such list for each sample in the batch)
print('Predicted:', decode_predictions(preds, top=5)[0])
decoded = imagenet_labels[np.argsort(preds)[0,::-1][:5]+1]

print("Result before saving:\n", decoded)

times = []
for i in range(20):
    start_time = time.time()
    preds = model.predict(x)
    delta = (time.time() - start_time)
    times.append(delta)
mean_delta = np.array(times).mean()
fps = 1 / mean_delta
print('average(sec):{:.2f},fps:{:.2f}'.format(mean_delta, fps))
