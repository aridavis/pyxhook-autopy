import pyxhook
import os

#get("mouse_log_file") -> Jikalau ada environment variables
mouse_log_file = os.environ.get("mouse_log_file", os.path.expanduser("~/Desktop/MouseLogger.log"))


def onMouseEvent(event):
    #membuka file mouse_log_file dengan mode a (append)
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