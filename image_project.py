import cv2
import numpy as np
def cartoonImage(image_path):
    
    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(img, 9, 300, 300)
    cartoon = cv2.bitwise_and(color, color, mask=edges)


    cv2.imshow('Original Image', img)
    cv2.imshow('Cartoon Image', cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_path = 'C:\\Users\\HP\\Desktop\\salman.jpg'
cartoonImage(image_path)