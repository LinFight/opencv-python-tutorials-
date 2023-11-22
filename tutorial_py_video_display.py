import cv2 as cv

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
cap.set(cv.CAP_PROP_FPS, 30)
print("摄像头的帧率是{}".format(cap.get(cv.CAP_PROP_FPS)))

# 死循环，逐帧读取摄像头信息
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
