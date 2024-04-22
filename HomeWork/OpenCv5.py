import cv2

cap = cv2.VideoCapture(0)
print("width: %d, height:  %d" % (cap.get(3), cap.get(4)))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
print("resized width: %d, height: %d"% (cap.get(3), cap.get(4)) )
while cap.isOpened():
    ret, img = cap.read()
    if ret:
        cv2.imshow('camera-0', img)
        if cv2.waitKey(10) & 0xFF == 27: #esc 프레임 조절
            break
    else:
        print('no camera!')
        break
cap.release()
cv2.destroyAllWindows()