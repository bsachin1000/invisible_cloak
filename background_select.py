
import cv2                              

cap = cv2.VideoCapture(0)               

                                       

while cap.isOpened():                   
    ret, back = cap.read()              
    if ret:                             
        cv2.imshow("img", back)         
        if cv2.waitKey(5) == ord(' '):
            cv2.imwrite('img.jpg', back)
                                        
            break

cap.release()                           
cv2.destroyAllWindows()                 
