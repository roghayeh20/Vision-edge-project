import cv2

image = cv2.imread("../images/input.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,100,200)

cv2.imwrite("../images/output.jpg",edges)



##اینجا فیچر بلر رو اد میکنیم
blur = cv2.GaussianBlur(gray,(5,5),0)

edges = cv2.Canny(blur,100,200)