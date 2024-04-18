import cv2
import os

print(os.getcwd())
print(os.path.dirname(__file__))

img_file = "img/img/model.jpg" #파일경로 변경 가능
img = cv2.imread(img_file) #영상로딩

if not img is None:
    cv2.imshow('IMG', img) #IMG라는 윈도우 생성,영상 보여주기
    while True:
        key = cv2.waitKey(0) #키보드 입력대기
        if key == 27:  #ESC 키 입력 검사
            cv2.destroyAllWindows() #윈도우 소멸
            break
else:
    print('No image file.')