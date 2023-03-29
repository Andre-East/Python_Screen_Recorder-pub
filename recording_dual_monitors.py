# All modules needed for this code 
from PIL import ImageGrab
import numpy as np
import cv2
import ctypes
from datetime import datetime
import time
from functools import partial
import keyboard
from plyer.utils import platform
from plyer import notification
from pathlib import Path



# These lines are used to get the resolution of the monitors from windows  
user32 = ctypes.windll.user32
# This line is used to get the combined width of both monitors 
width = user32.GetSystemMetrics(78)
# This line is used to get the combined height of both monitors 
height = user32.GetSystemMetrics(79)
# This line ensure that both monitors are recorderd when "ImageGrab.grab" is called 
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

# This line is used to get the current time and date of the sime the script is executed  
time_stamp = datetime.now().strftime('%Y-%m-%d_%H-%M')

#this line created the file name with the time stamp appended 
name = 'screen_record'+time_stamp

# This line is used to create the file in the directory of choice 
file_name = f'{name}.mp4'


# This line is used to render the video file format 
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

# This line is used to write/create the video 
captured_video = cv2.VideoWriter(file_name, fourcc, 7.9, (width, height))

# Vairables that will be intialized to help manage the speed of the recording
fps = 60
prev = 0

# This while loop will continuously take screenshots/record video until we end the recording 
while True:
    # This line is used store the time the loop began  
    time_elapsed = time.time() - prev
 
    if time_elapsed > 1.0/fps:

        prev = time.time()

        # This line is used to get the recorded area and store it 
        img = ImageGrab.grab(bbox=(0, 0, width, height))

        # This line is used to create an array with the screenshots that were taken 
        img_np = np.array(img)

        # This line is used to cnvert the color format from "BRG" which is is what
        # was originally recroded as to "RGB" which our displays recognize 
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

        # This line is used to write or to continues add the screenshots to the file 
        # in order to create a continuous video 
        captured_video.write(img_final)

        # This bool is then used to end the recording/stop screenshots 
        if cv2.waitKey(1) and keyboard.is_pressed('q'):
            break
# We then go ahead and destroy all windows      
cv2.destroyAllWindows()

# We also relase the view that was created from the script/app   
captured_video.release()

# This if is used to check if the file actually exists after the video had been completed and then 
# displays a message via windows toast notifications, and if not it promps that file was not saved. 
if not Path(file_name).is_file():
    notification.notify(
        title='Failed Saved',
        message= name+' has not been saved',
        app_name='PY Screen Recorder',
        app_icon=r'\path\to\python_94570.ico')    
else:
    notification.notify(
        title='Sucessfully Saved',
        message= name+' has been saved',
        app_name='PY Screen Recorder',
        app_icon=r'\path\to\python_94570.ico')