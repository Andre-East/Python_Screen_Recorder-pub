# All required modules 
from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
from datetime import datetime

# These lines are used to store the combined height and width of the monitors 
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)


# This line is used to get the date and time of the time the script was executed to be added to the
# name string of the the video that will be created 
time_stamp = datetime.now().strftime('%Y-%m-%d_%H-%M')

# This line is used to create the file name/ string 
file_name = f'screenrecord-{time_stamp}.mp4'

# This line is used to create/set the codec (vidoe format) that the file will be saved as 
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

# This line is used to creat the videos 
captured_video = cv2.VideoWriter(file_name, fourcc, 8.6, (width, height))

# This while look is used to continuely record the screen until you exit/terminate the code 
while True:
    # This line is used grab/record screenshots of the monitor 
    img = ImageGrab.grab(bbox=(0, 0, width, height))

    # This line is used to create an array of images to be used for as the video 
    img_np = np.array(img)

    # This line is used to convert the images from BGR to RGB colors 
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

    # This line is used to display the live feed of the screen 
    cv2.imshow('Screen Rec PY', img_final)

    # This line is used to write the video to the screen 
    captured_video.write(img_final)

    # This is bool is used to quick/terminate the script/app 
    if cv2.waitKey(1) == ord('q'):
        break

# These lines are used to clean up 
cv2.destroyAllWindows()
captured_video.release()