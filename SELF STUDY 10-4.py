from tkinter import *
from tkinter import messagebox

def keyEvent(event):
    arrow_keys = {37: "왼쪽 화살표", 38: "위쪽 화살표", 39: "오른쪽 화살표", 40: "아래쪽 화살표"}
    if event.state & 0x0001 and event.keycode in arrow_keys:
        messagebox.showinfo("키보드 이벤트", f"눌린 키 : Shift + {arrow_keys[event.keycode]}")

window = Tk()
window.bind("<KeyPress>", keyEvent)
window.mainloop()