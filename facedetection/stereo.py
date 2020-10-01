import numpy as np
import torch
import cv2
from blazeface import BlazeFace

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
print("PyTorch version:", torch.__version__)
print("CUDA version:", torch.version.cuda)
print("cuDNN version:", torch.backends.cudnn.version())

gpu = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(gpu)

net = BlazeFace().to(gpu)
net.load_weights("blazeface.pth")
net.load_anchors("anchors.npy")
# let's start the capture now
print("starting camera now....")


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    openCV = frame.copy()
    blaze = frame.copy()

    # possible to do threading here, but what ever..
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
    	# Display the resulting frame
	    cv2.rectangle(openCV, (x, y), (x+w, y+h), (255, 0, 0), 2)
  
    img = cv2.resize(frame,(128,128))
    detections = net.predict_on_image(img)
    if isinstance(detections, torch.Tensor):
        detections = detections.cpu().numpy()

    if detections.ndim == 1:
        detections = np.expand_dims(detections, axis=0)
    print("Found %d faces" % detections.shape[0])
    if detections.shape[0] > 0 :
        for i in range(detections.shape[0]):
            # adjust the coordinates to the original image
            ymin = detections[i, 0] * frame.shape[0]
            xmin = detections[i, 1] * frame.shape[1]
            ymax = detections[i, 2] * frame.shape[0]
            xmax = detections[i, 3] * frame.shape[1]
            cv2.rectangle(blaze, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (255, 0, 0), 2)
    # Display the resulting frame
    cv2.imshow('OpenCV',openCV)
    cv2.imshow('DL',blaze)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
