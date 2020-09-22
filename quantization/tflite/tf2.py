import argparse
import time
import numpy as np
from PIL import Image
import collections
import operator
import tensorflow as tf
import tensorflow_hub as hub

Class = collections.namedtuple('Class', ['id', 'score'])

# Models 
#   https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/2
#   https://tfhub.dev/google/efficientnet/b0/classification/1
#   
#
#
#

def get_output(scores, top_k=1, score_threshold=0.0):
  """Returns no more than top_k classes with score >= score_threshold."""
  
  classes = [
      Class(i, scores[i])
      for i in np.argpartition(scores, -top_k)[-top_k:]
      if scores[i] >= score_threshold
  ]
  return sorted(classes, key=operator.itemgetter(1),reverse=True)

#simple way to start
def runClass(classifier_url,image,runCount,k,threshold,height,width):
    # number of classes to return
    k = 1
    IMAGE_SHAPE = (height, width)
    # setup the path to the labels
    labels_path = tf.keras.utils.get_file('ImageNetLabels.txt','https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt')
    if ("mobilenet_v" in classifier_url):
        #print("Mobilenet detected, using url and not module")
        IMAGE_SHAPE = (224, 224)
        
    elif ("inception_v3" in classifier_url):
        #print("Inception_v3 detected, using url and not module")
        IMAGE_SHAPE = (299, 299)
   
    classifier = tf.keras.Sequential([
        hub.KerasLayer(classifier_url, input_shape=IMAGE_SHAPE+(3,))])
    # setup for probability vs raw scores
    probability_model = tf.keras.Sequential([classifier, 
                                         tf.keras.layers.Softmax()])
    theImage = Image.open(image).resize(IMAGE_SHAPE)

    theImage = np.array(theImage)/255.0
    print("First inference may be slower")
    for _ in range(runCount):
        start = time.perf_counter()
        result = probability_model.predict(theImage[np.newaxis, ...])
        resultLength = len(result[0])
        inference_time = time.perf_counter() - start
        print('%.1fms' % (inference_time * 1000))
        predicted_class = np.argmax(result[0], axis=-1)

    imagenet_labels = np.array(open(labels_path).read().splitlines())
    # some of the TF Models, e.g. efficientnet, assume the second line is index 0.
    # so we need to adjust
    offset = 0
    if resultLength < len(imagenet_labels):
        offset = 1
        predicted_class = predicted_class + 1

    classes =  get_output(result[0],k,threshold)
    print("")
    print('Label: Confidence')
    
    for klass in classes:
        pc = klass.id + offset
        print('%s: %.5f' % (imagenet_labels[pc],klass.score))

    return


def main():
    print("TF 2 testing")
    parser = argparse.ArgumentParser(
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
      '-m', '--model', required=True, help='url of the hub model to use')
   
    parser.add_argument(
      '-i', '--image', required=True, help='image to use')

    parser.add_argument(
      '-k', '--top_k', type=int, default=1,
      help='Max number of classification results')
    parser.add_argument(
      '-t', '--threshold', type=float, default=0.0,
      help='Classification score threshold')
    parser.add_argument(
      '-c', '--count', type=int, default=5,
      help='Number of times to run inference')

    parser.add_argument(
      '--height', type=int, default=299,
      help='height of image')
    parser.add_argument(
      '-w', '--width', type=int, default=299,
      help='width of image')
    args = parser.parse_args()
    
    runClass(args.model,args.image,args.count,args.top_k,args.threshold,args.height,args.width)


if __name__ == '__main__':
  main()
