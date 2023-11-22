import cv2 as cv
import sys

# 通过文件路径+文件名，读取图片文件
img = cv.imread("./samples/starry_night.jpg")

# 检测是否读取到图片，测试下来如果上一步没有读取到图片,直接给warning
if img is None:
    sys.exit("Could not read the image.")

# GUI 功能，winname 是窗口的名字
cv.imshow("Display window", img)

# 检测一次检测输入
k = cv.waitKey(0)

# 如果按键是s就将图片写到指定目录,ord 这个函数对键盘控制很有用
if k == ord("s"):
    cv.imwrite("./output/starry_night.png", img)
