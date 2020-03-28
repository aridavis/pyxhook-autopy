import pyxhook
import os

def onMouseEvent(event):
    #membuka file mouse_log_file dengan mode a (append)
    with open('mouselogger.log', 'a') as f :
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
