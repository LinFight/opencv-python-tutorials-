import cv2 as cv
import time

# 打开摄像头
cap = cv.VideoCapture("http://pinode1.local:8080?action=stream")  # 0表示默认摄像头，如果有多个摄像头可以尝试其他编号
# 判断摄像头是否打开
if not cap.isOpened():
    print("Cannot open camera")
    exit()

print("摄像头的像素是{}*{}".format(cap.get(cv.CAP_PROP_FRAME_WIDTH), cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
print("摄像头的帧率是{}".format(cap.get(cv.CAP_PROP_FPS)))

# 初始化背景模型
first_frame = cv.cvtColor(cap.read()[1], cv.COLOR_BGR2GRAY)
# 记录这一帧的时间
first_frame_time = time.time()

# 循环处理视频流
while True:
    # 记录现在的时间
    current_time = time.time()
    # 读取这一帧
    ret, frame = cap.read()
    # 如果读取失败，直接结束循环，然后结束程序
    if not ret:
        break

    # 转换为灰度图像
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # 计算当前帧与背景帧的时间差，用于计算速度
    frame_time = current_time - first_frame_time
    first_frame_time = current_time

    # 计算帧率并输出速度
    # frame_rate = 1 / frame_time  # 帧率 = 1 / 时间差
    # print(f"当前帧率：{frame_rate:.2f}fps")  # 保留两位小数

    # 计算物体移动速度并输出到图像右上角
    frame_diff = cv.absdiff(first_frame, gray)
    _, thresh = cv.threshold(frame_diff, 30, 255, cv.THRESH_BINARY)
    contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv.contourArea(contour) < 1000:  # 过滤掉较小的轮廓
            continue
        x, y, w, h = cv.boundingRect(contour)
        speed = w / frame_time  # 速度 = 宽度 / 时间差
        cv.putText(frame, f"{speed:.2f}", (x, y - 15), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0),
                   2)  # 将速度写在右上角，这里保留了小数点后两位，其余和绘制轮廓的操作一样
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 显示结果
    cv.imshow("高空抛物检测", frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
