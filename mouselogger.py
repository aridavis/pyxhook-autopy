import pyxhook
import os

mouse_log_file = os.environ.get("mouse_log_file", os.path.expanduser("~/Desktop/MouseLogger.log"))

def onMouseEvent(event):
    with open(mouse_log_file, 'a') as f :
        f.write(str(event.WindowName))
        f.write(str(event.Position))
        f.write(str(event.MessageName))
        f.write("===========================\n\n")

hook = pyxhook.HookManager()

hook.MouseMovement = onMouseEvent

hook.HookMouse()


try:
    hook.start()
except :
    pass