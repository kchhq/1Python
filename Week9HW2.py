from tkinter import *
import random 

btnList = [None] * 9
fnameList = ["froyo.gif", "gingerbread.gif", "honeycomb.gif", "iocecream.gif", 
             "jellybean.gif", "kitkat.gif", "lollipop.gif", "arshmallow.gif", "nought.gif"]

random.shuffle(fnameList)

photoList = [None] * 9

window = Tk()
window.geometry("210x210")

for i in range(9):
    photoList[i] = PhotoImage(file="desktop/mysmallcode/1python/" + fnameList[i])
    btnList[i] = Button(window, image=photoList[i])

num = 0
for i in range(3):
    for k in range(3):
        btnList[num].place(x=k*70, y=i*70)
        num += 1

window.mainloop()
