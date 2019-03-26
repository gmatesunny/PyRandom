import cv2

cap = cv2.VideoCapture(0, cv2.CAP_V4L)
while(True):
    ret, frame = cap.read()
    gray = cv2.medianBlur(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY),5)
    circles=cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100)

    if circles != None:
        circles = circles[0, :].astype("int")
        for (x, y, r) in circles:
            cv2.circle(frame, (x, y), r, (100,10,1), 25)
       
    cv2.imshow("video", frame)
    if cv2.waitKey(1)==27:# esc Key
        break
        
cap.release()
cv2.destroyAllWindows()
