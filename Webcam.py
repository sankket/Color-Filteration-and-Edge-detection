import cv2
import matplotlib.pyplot as plt
#for accessing The Webcam we use Video Capture Function.
cap = cv2.VideoCapture(0)
#if Video capture is open
if cap.isOpened():
    #Reading input from The camera.
    ret, frame = cap.read()
    print(ret)
    print(frame)

else:
    ret = False
#Changing To RGB colour Frame.
img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#displaying Images
plt.imshow(img1)
plt.title("Camera Image-1")
plt.xticks([])
plt.yticks([])
plt.show()
cap.release()
