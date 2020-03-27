import autopy
import os
import time

# Ngescreenshot
bitmap = autopy.bitmap.capture_screen()

# Menyimpan dalam format timestamp.png
bitmap.save( str(round(time.time())) +".png")
