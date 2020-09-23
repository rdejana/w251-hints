import tensorflow as tf
import numpy as np

loaded = tf.saved_model.load("/Users/rdejana/Downloads/efficientnet_b1_classification_1")

file = tf.keras.utils.get_file(
    "grace_hopper.jpg",
    "https://storage.googleapis.com/download.tensorflow.org/example_images/grace_hopper.jpg")
img = tf.keras.preprocessing.image.load_img(file, target_size=[224, 224])

labels_path = tf.keras.utils.get_file(
    'ImageNetLabels.txt',
    'https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt')
imagenet_labels = np.array(open(labels_path).read().splitlines())




print(list(loaded.signatures.keys())) 

infer = loaded.signatures["serving_default"]
print(infer.structured_outputs)
x = tf.keras.preprocessing.image.img_to_array(img)
x = x[tf.newaxis,...]

labeling = infer(tf.constant(x)) #[pretrained_model.output_names[0]]
print(labeling)
decoded = imagenet_labels[np.argsort(labeling)[0,::-1][:5]+1]
