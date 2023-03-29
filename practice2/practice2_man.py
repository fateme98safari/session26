import cv2

man_pic = cv2.imread("spaces_u9ESMkINnUK9Z0nC4FPH_uploads_zjIFbzgo6jfEpy534tEl_2.webp")
invert = cv2.bitwise_not(man_pic)
cv2.imshow("",invert)
cv2.imwrite("man_pic.jpg",invert)

cv2.waitKey()