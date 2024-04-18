import cv2
video_file = "img/img/big_buck.avi"

cap = cv2.VideoCapture(video_file)
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

