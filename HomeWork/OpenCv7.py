import cv2
import numpy as np
#리스트는 데이터 타입이 없음 리스트는 연속된 메모리얼에 들어가는게 아님
img = cv2.imread('img/img/blank_500.jpg')
list1 = [[50,50],[150,150],[100,140],[200,240]]
pts1 = np.array(list1,dtype = np.int32)
list2 = [pts1]
print(len(list1),pts1.shape,len(list2)) #list2안에있는 list1은 4개가 들어있꼬 4행2열 list2는 1개

pts1 = np.array([[50,50], [150,150], [100,140],[200,240]], dtype=np.int32) #리스트안에 있는 타입이 int
pts2 = np.array([[350,50], [250,200], [450,200]], dtype=np.int32)
pts3 = np.array([[150,300], [50,450], [250,450]], dtype=np.int32)
pts4 = np.array([[350,250], [450,350], [400,450],[300,450], [250,350]],dtype=np.int32)

cv2.polylines(img, [pts1], False, (255,0,0))
cv2.polylines(img, [pts2], False, (0,0,0), 10)
cv2.polylines(img, [pts3], True, (0,0,255), 10)
cv2.polylines(img, [pts4], True, (0,0,0))

cv2.imshow('polyline', img)
cv2.waitKey(0)
cv2.destroyAllWindows()