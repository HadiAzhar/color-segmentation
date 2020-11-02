#!/usr/bin/env python
# coding: utf-8

import cv2
import numpy as np

image = cv2.imread('images/sc2.jpg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
blur = cv2.medianBlur(hsv ,11)

lower = np.array([25,43,128])
upper = np.array([33,163,179])

mask = cv2.inRange(blur, lower, upper)
res = cv2.bitwise_and(image,image, mask= mask)            
res = np.where(res == 0, 255, res)
cv2.imshow("mask ",mask)
cv2.imshow('stack', np.hstack([image, res]))
cv2.waitKey(0)

cv2.imwrite("mask.jpg", mask)
cv2.imwrite("result.jpg", res)


