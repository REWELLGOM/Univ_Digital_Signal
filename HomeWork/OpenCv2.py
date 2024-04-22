import cv2

img_file = "photo.jpg"
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
cv2.imshow("my darling daughter", img)

key = cv2.waitKey(0) & 0xFF
if key == 27: #esc
     cv2.destroyAllWindows()
elif key == ord('s'):
     print('saving file.')
     cv2.imwrite("./gray.jpg", img)
     cv2.destroyAllWindows()
