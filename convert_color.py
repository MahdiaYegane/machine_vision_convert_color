import cv2

img = cv2.imread("images/img2.jpg")

convert_color=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

cv2.imshow("orginal",img)
cv2.imshow("convert_color",convert_color)

cv2.waitKey(0)
cv2.destroyAllWindows()
