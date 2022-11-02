import tkinter
import pywintypes
import win32api
import win32con
from random import choice

early = ["Where Is Jungle?", "When Is Objective?", "Runes Up?", "Can You Fight?", "Where Should You Stand?",
         "Should You Push?", "Are You Strong?"]

label = tkinter.Label(text="", font=('Franklin Gothic Heavy', '60'), fg='white', bg='grey')
label.master.overrideredirect(True)
label.master.geometry("+650+100")
label.master.lift()
label.master.wm_attributes("-topmost", True)
label.master.wm_attributes("-disabled", True)
label.master.wm_attributes("-transparentcolor", "grey")
label.master.wm_attributes("-alpha", 0.5)
hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))
exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
label.pack()


def update():
    label['text'] = choice(early)
    label.after(10000, update)


update()
label.mainloop()
