# python_screen_recorder

## Description/Usage

This is a beginner level python project that I created to record my other projects. It is a commandline executable Python screen recorder (without audo) for Windows enviroments.

![sample5](https://user-images.githubusercontent.com/68747084/230796396-5dcfda01-609c-487e-811c-b21fecf12637.gif)

## Instructions
<ul>
<li>Simply copy the script and save it as a ".py" file as well as the icon in the "icon" folder.</li>
<li>Update the absolute path for the the icon "icon=r..."</li> 

<img src="https://user-images.githubusercontent.com/68747084/230797965-ac31bd7b-d50e-4b2e-86fd-7a8a0e9894f4.png" width="500px" height="400px">

<li>Update the absolute path for where the recordings are stored</li> 

<li>You exceute it from the terminal by calling <b>python "\path\to\file\py_script_name.py"</b>.</li>

<li>Once your are done recording hit the "q" key to terminate or end the script/recording.</li>
</ul>

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




