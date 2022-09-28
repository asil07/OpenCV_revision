import  cv2
import numpy as np

img = cv2.imread("img.jpg")
print(img.shape)


imgResize = cv2.resize(img, (500, 600))
print(imgResize.shape)

imgCropped = img[70:250, 300:550]

cv2.imshow("original", img)
# cv2.imshow("img-resize", imgResize)
cv2.imshow("img-Cropped", imgCropped)




cv2.waitKey(0)







