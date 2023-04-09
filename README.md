# python_screen_recorder

## Description/Usage

This is a beginner level python project that I created to record my other projects. It is a commandline executable Python screen recorder (without audo) for Windows enviroments.

![sample5](https://user-images.githubusercontent.com/68747084/230796396-5dcfda01-609c-487e-811c-b21fecf12637.gif)

## Instructions

Simply copy the script and save it as a ".py" file as well as the icon in the "icon" folder.
Update the absolute path for the the icon 

<!-- ![update_for_icon](https://user-images.githubusercontent.com/68747084/230797280-845e9f55-8f6a-4267-a93c-622b5637058c.png ) -->

<img src="https://user-images.githubusercontent.com/68747084/230797280-845e9f55-8f6a-4267-a93c-622b5637058c.png" width="400px" height="200px">


<!-- ![update_for_icon2](https://user-images.githubusercontent.com/68747084/230797281-f2400349-a5a7-4fbc-9214-e1f4da17e074.png) -->

Update the absolute path for where the recordings are stored 

You exceute it from the terminal by calling <b>python "\path\to\file\py_script_name.py"</b>.

Once your are done recording hit the "q" key to terminate or end the script/recording.


## Required Modules
```python
from PIL import ImageGrab 
import numpy as np
import cv2 
import ctypes 
from datetime import datetime 
import time 
from functools import partial
import keyboard
from winotify import Notification, audio
from pathlib import Path
```

## Note

You will need to update the path to 

<hr>
Open to any suggestions that can improve the performance




