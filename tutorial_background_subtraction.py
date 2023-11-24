import cv2 as cv

back_sub = cv.createBackgroundSubtractorMOG2()

# 选取系统第一个摄像头
cap = cv.VideoCapture(0)
# 判断摄像头是否打开
if not cap.isOpened():
    print("Cannot open camera")
    exit()

print("摄像头的像素是{}*{}".format(cap.get(cv.CAP_PROP_FRAME_WIDTH), cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
print("摄像头的帧率是{}".format(cap.get(cv.CAP_PROP_FPS)))

# 设置摄像头长宽像素
cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
print("摄像头的像素是{}*{}".format(cap.get(cv.CAP_PROP_FRAME_WIDTH), cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
# 设置摄像头的帧率
cap.set(cv.CAP_PROP_FPS, 120)
print("摄像头的帧率是{}".format(cap.get(cv.CAP_PROP_FPS)))
