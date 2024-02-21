import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('dx.jpg')
image_bgr = cv.cvtColor(img, cv.COLOR_RGB2BGR)

# set figure size
plt.figure(figsize=(20, 20))

# show the first image
plt.subplot(221)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.axis("off")

# show the second image
sobelx = cv.Sobel(src=blur_img, ddepth=cv.CV_64F, dx=1, dy=0, ksize=5)
filtered_image_x = cv.convertScaleAbs(sobelx)

plt.subplot(222)
plt.imshow(img, cmap='gray')
plt.title('SobelX')
plt.axis("off")

# show the third image
sobely = cv.Sobel(src=blur_img, ddepth=cv.CV_64F, dx=0, dy=1, ksize=5)
filtered_image_y = cv.convertScaleAbs(sobely)


plt.subplot(223)
plt.imshow(img, cmap='gray')
plt.title('SobelY')
plt.axis("off")

# show the fourth image
sobelxy = cv.Sobel(src=blur_img, ddepth=cv.CV_64F, dx=1, dy=1, ksize=5)
filtered_image_xy = cv.convertScaleAbs(sobelxy)

plt.subplot(224)
plt.imshow(img, cmap='gray')
plt.title('SobelXY')
plt.axis("off")

# show the frame
plt.show()


