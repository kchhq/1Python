from tkinter import *
from time import *

fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif",
             "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]
photoList = [None] * 9
num = 0

def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    updatePhoto()

def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    updatePhoto()

def updatePhoto():
    photo = PhotoImage(file="desktop/mysmallcode/1python" + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    nameLabel.config(text=fnameList[num]) 

## 메인 코드 부분 ##
window = Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = Button(window, text="<< 이전", command=clickPrev)
btnNext = Button(window, text="다음 >>", command=clickNext)

photo = PhotoImage(file="desktop/mysmallcode/1python" + fnameList[0])
pLabel = Label(window, image=photo)

nameLabel = Label(window, text=fnameList[0], font=("Arial", 12))

btnPrev.place(x=200, y=10)
nameLabel.place(x=320, y=15) #셀프스터디 추가
btnNext.place(x=450, y=10)
pLabel.place(x=15, y=50)

window.mainloop()
