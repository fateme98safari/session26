import cv2
import numpy as np


rectangle = np.ones((300, 300), dtype="uint8")
rectangle[0:300 , 0:300]=255
rectangle[10:255,40:60]=rectangle[10:30,40:195]=rectangle[110:130,40:180]=0

cv2.imshow("", rectangle)
cv2.imwrite("result.jpg", rectangle)
cv2.waitKey()