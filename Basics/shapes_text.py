import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# print(img)
# img[:] = 255, 0, 0

cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 255, 0), thickness=3)
cv2.rectangle(img, (0,0), (250, 350), (0, 0, 255),  cv2.FILLED)
cv2.circle(img, center=(400, 50), radius=30, color=(255, 255, 0), thickness=5)
cv2.putText(img, "Opencv ASIL", (300, 200), cv2.FONT_HERSHEY_COMPLEX, fontScale=1,
            color=(0, 150, 0), thickness=1)



cv2.imshow("Image", img)






cv2.waitKey(0)