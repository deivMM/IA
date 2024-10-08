import cv2
import cvzone
import numpy as np


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

def empty(a):
    pass

# cvzone.findContours()

cv2.namedWindow('Settings')
cv2.resizeWindow('Settings', 640,240)
cv2.createTrackbar('Threshold1','Settings', 50,255, empty)
cv2.createTrackbar('Threshold2','Settings', 50,255, empty)


def preProcessing(img):
    imgPre = cv2.GaussianBlur(img, (5,5), 3)
    thres1 = cv2.getTrackbarPos('Threshold1', 'Settings')
    thres2 = cv2.getTrackbarPos('Threshold2', 'Settings')
    imgPre = cv2.Canny(imgPre, thres1 ,thres2)
    return imgPre

while True:
    succes, img = cap.read()
    imgPre = preProcessing(img)

    imgStacked = cvzone.stackImages([img, imgPre], 2, 1)
    cv2.imshow('Image', imgStacked)
    # cv2.imshow('Image_Pre', imgPre)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()