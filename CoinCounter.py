import cv2.cv2
from cv2 import cv2
import numpy as np

gaussValue = 3
valueKernel = 3

original = cv2.imread('image/monedas.jpg')
# Change color original image
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
# First delete noise for image
blur = cv2.GaussianBlur(gray, (gaussValue, valueKernel), 0)
canny = cv2.Canny(blur, 60, 100)

kernel = np.ones((valueKernel, valueKernel), np.uint8)
# MORPH_CLOSE delete noise inside image
close = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)


contours, hierarchy = cv2.findContours(close.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("coints: {}" .format(len(contours)))
cv2.drawContours(close)
# Open result image
cv2.imshow('image grey', gray)
cv2.imshow('Gauss', blur)
cv2.imshow('Canny', canny)
cv2.imshow('MORPH_CLOSE', close)
cv2.waitKey(0)
