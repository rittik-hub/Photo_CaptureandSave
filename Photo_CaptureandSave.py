## Photo Capture and save it to your machine
### Contributor : CHAUDHARY HAMDAN
###### All you need is once the camera window is opened after running the code, press space to capture the photo and 'q' to quit 

import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)
c = 0
prvdt_string
while True:
    ret,frame = cap.read()
    if ret == False:
        continue
    cv2.imshow('Frame',frame)
    key_pressed = cv2.waitKey(1) & 0xff
    if key_pressed == ord(' '):
        dt_string = datetime.now().strftime("%d%m%Y_%H%M%S")
        if prvdt_string == dt_string:
            c += 1
        else:
            prvdt_string = dt_string
            c = 0
        ans_string = dt_string+'_'+str(c)
        cv2.imwrite(filename=f'Photos_Captured/Hamdan_s_OpenCV_{ans_string}.jpg', img=frame)
    if key_pressed == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
