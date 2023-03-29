import cv2
# import matplotlib
two_men=cv2.imread("3.jpg")

result=cv2.rotate(two_men,cv2.ROTATE_180)
cv2.imshow("pic",result)
cv2.imwrite("happies_men.jpg",result)
cv2.waitKey()