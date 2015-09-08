import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
e1 = cv2.getTickCount()
# your code execution
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
'''

img1 = cv2.imread('messi.png')

e1 = cv2.getTickCount()
for i in xrange(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print t

# check if optimization is enabled
cv2.useOptimized()
# True

# %timeit res = cv2.medianBlur(img,49)
# 10 loops, best of 3: 34.9 ms per loop

# Disable it
cv2.setUseOptimized(False)
cv2.useOptimized()
# False

# %timeit res = cv2.medianBlur(img,49)
# 10 loops, best of 3: 64.1 ms per loop