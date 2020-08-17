import cv2

def sketch(image):
   #Converting a Image in grey for Edge detection.
    img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

   #Blurring the image for getting smooth image as well as reducing The noise.
    img_gray_blur = cv2.GaussianBlur(img_gray,(5,5),0)# Gaussian kernal values
   #canny function is used edge detection and accepts grey scale images.
    canny_edge = cv2.Canny(img_gray_blur, 40, 110)  # 10 is upper and 70 is lower threshold for hysterysis procedure.

   #Converting into Binary format
    ret, mask = cv2.threshold(canny_edge, 70, 255, cv2.THRESH_BINARY)

    return mask

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("Edge Detection in Python", sketch(frame))
    if cv2.waitKey(1) == 13:
        break
cap.release()
cv2.destroyAllWindows()
