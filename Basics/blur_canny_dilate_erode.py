import cv2
import numpy as np

img = cv2.imread("img.jpg")
kernel = np.ones((5,5), np.uint8)


imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(imgBlur, 100, 100)
imgDilate = cv2.dilate(imgCanny, kernel=kernel, iterations=1)
imgErode = cv2.erode(imgDilate, kernel, iterations=1)



cv2.imshow("img gray", imgGray)
cv2.imshow("img Blur", imgBlur)
cv2.imshow("img Canny", imgCanny)
cv2.imshow("img dilate", imgDilate)
cv2.imshow("img erosion", imgErode)
cv2.waitKey(0)
