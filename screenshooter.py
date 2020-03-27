import autopy
import os
import time

bitmap = autopy.bitmap.capture_screen()
bitmap.save( str(round(time.time())) +".png")
