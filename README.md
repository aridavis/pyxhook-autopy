# Pyxhook & Autopy Example

## Pyxhook
**Pyxhook** adalah library python yang menyediakan callback untuk semua event mouse dan keyboard di Linux. Untuk versi windowsnya, nama librarynya adalah **Pyhook**

### Pyxhook Tutorial
1. **Inisialisasi Hook**
  Di tahap ini, kita harus melakukan inisialisasi dahulu terhadap hooknya dengan cara
   ```
   hook = pyxhook.HookManager()
   ```

2. **Memasukkan Fungsi Event Mouse/Keyboard**
   Di tahap ini, kita buat sebuah function dan kita assign nilai dari event dari mouse/keyboard menjadi function tersebut.
   ```
   def onMouseEvent(event):
   		...


   #set mouse movement
   hook.MouseMovement = onMouseEvent
   ```

3. **Mengaktifkan Hook**
   ```
   hook.HookMouse()
   hook.HookKeyboard()
   ```

4. **Menjalankan Hook**
   ```
   hook.start()
   ```

#### Event - Event Mouse Hook
##### source : https://sourceforge.net/p/pyhook/wiki/PyHook_Tutorial/

```
def OnMouseEvent(event):
    # called when mouse events are received
    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:',event.Time
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Position:',event.Position
    print 'Wheel:',event.Wheel
    print 'Injected:',event.Injected
    print '---'
```


#### Event - Event Keyboard Hook
##### source : https://sourceforge.net/p/pyhook/wiki/PyHook_Tutorial/

```
def OnKeyboardEvent(event):
    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:',event.Time
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Ascii:', event.Ascii, chr(event.Ascii)
    print 'Key:', event.Key
    print 'KeyID:', event.KeyID
    print 'ScanCode:', event.ScanCode
    print 'Extended:', event.Extended
    print 'Injected:', event.Injected
    print 'Alt', event.Alt
    print 'Transition', event.Transition
    print '---'
```


## Autopy
**Autopy** adalah library Python yang berguna untuk mengontrol mouse dan keyboard, mencari warna dan bitmap pada layar, dan memunculkan alert
Source : https://pypi.org/project/autopy/

Contoh Penggunaannya bisa dilihat di codingan screenshoter.py