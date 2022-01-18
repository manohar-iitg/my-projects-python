#importing the module
import cv2

#loading the image
img=cv2.imread("polygons.jpeg")

#converting BGR to HSV
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#defining a function to find the shapes
def getContours(img):
    #finding the contours
    contours , heirarchy = cv2.findContours(img , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
    
    #seperating for each contour and drawing the border of shape
    for cnt in contours:
        cv2.drawContours(imgContour , (cnt) , -1, (20,20,20) , 3)
        length=cv2.arcLength(cnt, True)
        
        #finding approx polynomial dynamics
        approx=cv2.approxPolyDP(cnt, 0.03*length, True)
        lenapp=len(approx)

        #defining x and y and setting to 0
        x=0
        y=0
        
        #to find x and y to write quadrilateral name
        for i in range(0,lenapp):
            #Taking coordinate of each corner approximated
            t=approx[i][0]
            s=str(t)
            s2=s[1:len(s)-1]
            k=s2.split()
            r1=int(k[0])
            x+=r1
            r2=int(k[1])
            y+=r2
        
        #Finding the avg x and y value to get approx centre    
        x2=int(x/lenapp)
        y2=int(y/lenapp)
        
        #conditions for the shape
        if len(approx)==3:
            cv2.putText(imgContour,'Triangle', (x2-50,y2), cv2.FONT_HERSHEY_TRIPLEX, 0.65, (255,255,255), 2)
        
        elif len(approx)==4:
            cv2.putText(imgContour,'Quadrilateral', (x2-50,y2), cv2.FONT_HERSHEY_TRIPLEX, 0.65, (255,255,255), 2)
        
        elif len(approx)==5:
            cv2.putText(imgContour,'Pentagon', (x2-50,y2), cv2.FONT_HERSHEY_TRIPLEX, 0.65, (255,255,255), 2)
        
        elif len(approx)==5:
            cv2.putText(imgContour,'Hexagon', (x2-50,y2), cv2.FONT_HERSHEY_TRIPLEX, 0.65, (255,255,255), 2)
        
        else:
            cv2.putText(imgContour,'Circle', (x2-30,y2), cv2.FONT_HERSHEY_TRIPLEX, 0.65, (255,255,255), 2)

#redcolor
h_min, h_max = 171,179
s_min, s_max= 156,255
v_min, v_max= 59, 255
lower= (h_min, s_min, v_min)
upper= (h_max, s_max, v_max)

mask=cv2.inRange(imgHSV, lower, upper)
result=cv2.bitwise_and(img, img, mask=mask)
imgContour = result.copy()
imgGray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 100)
imgCanny = cv2.Canny(imgBlur, 100, 200)

getContours(imgCanny)
cv2.imshow("img", img)
cv2.imshow("Red coloured objects", imgContour)
cv2.waitKey(0)
cv2.destroyAllWindows()

#greencolor
h_min, h_max = 67,90
s_min, s_max= 123,255
v_min, v_max= 138, 255
lower= (h_min, s_min, v_min)
upper= (h_max, s_max, v_max)

mask=cv2.inRange(imgHSV, lower, upper)
result=cv2.bitwise_and(img, img, mask=mask)
imgContour = result.copy()
imgGray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 100)
imgCanny = cv2.Canny(imgBlur, 100, 200)

getContours(imgCanny)
cv2.imshow("img", img)
cv2.imshow("Green coloured objects", imgContour)
cv2.waitKey(0)
cv2.destroyAllWindows()

#bluecolor
h_min, h_max = 97,109
s_min, s_max= 204,255
v_min, v_max= 113, 255
lower= (h_min, s_min, v_min)
upper= (h_max, s_max, v_max)

mask=cv2.inRange(imgHSV, lower, upper)
result=cv2.bitwise_and(img, img, mask=mask)
imgContour = result.copy()
imgGray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 100)
imgCanny = cv2.Canny(imgBlur, 100, 200)

getContours(imgCanny)
cv2.imshow("img", img)
cv2.imshow("Blue coloured objects", imgContour)
cv2.waitKey(0)
cv2.destroyAllWindows()

#yellowcolor
h_min, h_max = 21,40
s_min, s_max= 115,255
v_min, v_max= 128, 255
lower= (h_min, s_min, v_min)
upper= (h_max, s_max, v_max)

mask=cv2.inRange(imgHSV, lower, upper)
result=cv2.bitwise_and(img, img, mask=mask)
imgContour = result.copy()
imgGray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 100)
imgCanny = cv2.Canny(imgBlur, 100, 200)

getContours(imgCanny)
cv2.imshow("img", img)
cv2.imshow("Yellow coloured objects", imgContour)
cv2.waitKey(0)
cv2.destroyAllWindows()

#orangecolor
h_min, h_max = 6,19
s_min, s_max= 85,255
v_min, v_max= 180, 255
lower= (h_min, s_min, v_min)
upper= (h_max, s_max, v_max)

mask=cv2.inRange(imgHSV, lower, upper)
result=cv2.bitwise_and(img, img, mask=mask)
imgContour = result.copy()
imgGray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 100)
imgCanny = cv2.Canny(imgBlur, 100, 200)

getContours(imgCanny)
cv2.imshow("img", img)
cv2.imshow("Yellow coloured objects", imgContour)
cv2.waitKey(0)
cv2.destroyAllWindows()