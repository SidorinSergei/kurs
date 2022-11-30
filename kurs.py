import cv2
import numpy as np


def viewImage(image,name):
    cv2.namedWindow(''+name, cv2.WINDOW_NORMAL)
    cv2.imshow(''+name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

green = np.uint8([[[132, 197, 143 ]]])
green_hsv = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(green_hsv)

image = cv2.imread('list_1.jpg')
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
viewImage(hsv_img,'list') ## 1

green_low = np.array([40 ,84, 50] )
green_high = np.array([70, 255, 255])
curr_mask = cv2.inRange(hsv_img, green_low, green_high)
hsv_img[curr_mask > 0] = ([70,255,255])
viewImage(hsv_img,'list_1') ## 2

## Преобразование HSV-изображения к оттенкам серого для дальнейшего оконтуривания
RGB_again = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)
gray = cv2.cvtColor(RGB_again, cv2.COLOR_RGB2GRAY)
viewImage(gray,'list_gray') ## 3

ret, threshold = cv2.threshold(gray, 90, 255, 0)
viewImage(threshold,'list_maska') ## 4

contours, hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0, 0, 255), 3)
viewImage(image,'list_final') ## 5
