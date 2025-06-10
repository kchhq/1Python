from tkinter import *
from tkinter import messagebox

# 화살표 키 한글 매핑
arrow_map = {
    "Left": "왼쪽 화살표",
    "Right": "오른쪽 화살표",
    "Up": "위쪽 화살표",
    "Down": "아래쪽 화살표"
}

def keyEvent(event):
    if event.keysym in arrow_map:
        key_name = arrow_map[event.keysym]
        # Shift 눌리면 확인
        if event.state & 0x0001:
            msg = "눌린 키 : Shift + " + key_name
        else:
            msg = "눌린 키 : " + key_name
        messagebox.showinfo("키보드 이벤트", msg)

window = Tk()
window.bind("<Key>", keyEvent)
window.mainloop()
