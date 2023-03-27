# All required modules 
import cv2
import numpy as np
import pyautogui
import time
from datetime import datetime
import ctypes

# These lines are used to capture the resolution of the monitor  
user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height = user32.GetSystemMetrics(1)
screen_size = (width, height)


fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

# This line is used to get the current time and date of the sime the script is executed 
time_stamp = datetime.now().strftime('%Y-%m-%d_%H-%M')

#this line created the file name with the time stamp appended 
name = 'screen_record'+time_stamp

# This line is used to create the file in the directory of choice 
file_name = f'{name}.mp4'

# This line is used to write/create the video 
vid = cv2.VideoWriter(file_name, fourcc, 8.6, (screen_size))

# These libes set the speed of the recording 
fps = 60
prev = 0

# This while is used to continously record the screen 
while True:

    
    time_elapsed = time.time() - prev

    # This line is used to take screenshots of the screen 
    img = pyautogui.screenshot()

    # This bool is used to check if record speed is faster than the fps 
    if time_elapsed > 1.09/fps:
        prev = time.time()

        # This line is used to create an array with the screenshots that were taken 
        frame = np.array(img)

        # This line is used to cnvert the color format from "BRG" which was what
        # it was originally recroded as to "RGB" which our displays recognize 
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # This line is used to display the live feed of the screen
        cv2.imshow('Screen Rec PY', frame)

        # This line is used to write or to continues add the screenshots to the file 
        # in order to create a continuous video 
        vid.write(frame)

    # This bool is then used to end the recording/stop screenshots 
    if cv2.waitKey(10) == ord('q'):
        break

# These lines are used to clean up    
cv2.destroyAllWindows()
vid.release()