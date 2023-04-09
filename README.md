# python_screen_recorder

## Description/Usage

This is a beginner level python project that I created to record my other projects. It is a commandline executable Python screen recorder (without audo) for Windows enviroments.

![sample5](https://user-images.githubusercontent.com/68747084/230796396-5dcfda01-609c-487e-811c-b21fecf12637.gif)

## Instructions
<ul>
<li>Simply copy the script and save it as a ".py" file as well as the icon in the "icon" folder.</li>
<li>Update the absolute path for the the icon that is used in the windows toater notification</li> 

<img src="https://user-images.githubusercontent.com/68747084/230797965-ac31bd7b-d50e-4b2e-86fd-7a8a0e9894f4.png" width="550px" height="400px">

<li>Update the absolute path for where the recordings are stored</li> 

<li>You exceute it from the terminal by calling <b>python "\path\to\file\py_script_name.py"</b>.</li>

<li>Once your are done recording hit the "q" key to terminate or end the script/recording.</li>
</ul>




## Required Modules
```python
from PIL import ImageGrab      #https://pypi.org/project/Pillow/ 
import numpy as np     #https://numpy.org/
import cv2      #https://pypi.org/project/opencv-python/
import ctypes     #https://docs.python.org/3/library/ctypes.html
from datetime import datetime      #https://docs.python.org/3/library/datetime.html
import time     #https://docs.python.org/3/library/time.html
from functools import partial      #https://docs.python.org/3/library/functools.html
import keyboard     #https://pypi.org/project/keyboard/
from winotify import Notification, audio       #https://pypi.org/project/winotify/
from pathlib import Path     #https://docs.python.org/3/library/pathlib.html
```



## Features
<ul>
<li>Allows recording for a dual monitor recording for monitors of different dimensions</li>
<li>Continous recording until terminations</li>
<li>Script can be mondified to store video file in a different location</li> 
<li>Provides a windows toast notification upon completion of recording (whether files saved succesfully or failed)</li>
</ul>



<hr>
Open to any suggestions that can improve the performance




