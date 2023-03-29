import cv2

girl_pic = cv2.imread("spaces_u9ESMkINnUK9Z0nC4FPH_uploads_n1fj3dyqbjER3SLYexIW_1.webp")
invert = cv2.bitwise_not(girl_pic)
cv2.imshow("",invert)
cv2.imwrite("girl_pic.jpg",invert)

cv2.waitKey()
