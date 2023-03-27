# All required modules 
import mss
import cv2
import numpy as np

# This function is used to take a screen shot of the second monitor and returns the  image 
def secondmonitor():
    with mss.mss() as sct:
        
        # Get information of monitor 2
        monitor_number = 2
        mon = sct.monitors[monitor_number]

        # The this sects an object that contains details for the monitor to be captured
        monitor = {
            "top": mon["top"],
            "left": mon["left"],
            "width": mon["width"],
            "height": mon["height"],
            "mon": monitor_number
        }
               
        # Grab the data
        sct_img = sct.grab(monitor)
        img = np.array(sct.grab(monitor)) # BGR Image
        return cv2.imshow("OpenCV", img)
        
        
# This whiel loop will call the second monitor function until the user quits/terminates the script/app 
while True:
    secondmonitor()
    if cv2.waitKey(10) == ord('q'):
        break