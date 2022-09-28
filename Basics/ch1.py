import cv2


# img = cv2.imread("img.jpg")
#
# cv2.imshow("out", img)
# cv2.waitKey(0)

cap = cv2.VideoCapture(1)

cap.set(3, 640)
cap.set(4, 420)
# cap.set(10, 10) # brightness

while True:
    success, img = cap.read()
    cv2.imshow("vid", img)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break


