import cv2
video_file = "img/img/big_buck.avi"

cap = cv2.VideoCapture(video_file)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,320)
nframe = cap.set(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int (500/fps)
cap.set(cv2.CAP_PROP_POS_MSEC,int(nframe*fps)//2)
print("FPS: %f, Delay: %dms" %(fps, delay))

while cap.isOpened():
    ret, img = cap.read()
    if ret:
        cv2.imshow(video_file, img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        print('no more frame.')
        break
else:
    print('cant open video.')
cap.release()
cv2.destroyAllWindows()

