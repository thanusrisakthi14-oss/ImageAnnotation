import cv2
import matplotlib.pyplot as plt
image = cv2.imread("baby_2.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
cv2.rectangle(image, (20, 20), (170, 170), (0, 255, 255), 3)
cv2.circle(image, (100, 100), 15, (0, 255, 255), 3)
cv2.line(image, (20, 20), (170, 170), (0, 255, 255), 3)
cv2.putText(image,"Baby",(20,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)
plt.imshow(image)
plt.show()