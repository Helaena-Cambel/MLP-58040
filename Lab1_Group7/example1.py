import cv2

img = cv2.imread("larva.jpg", cv2.IMREAD_COLOR)

cv2.imshow("larva.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
