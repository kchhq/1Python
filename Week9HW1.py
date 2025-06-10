from tkinter import *

window = Tk()

photo1 = PhotoImage(file="desktop/mysmallcode/1python/pic1.gif")
photo2 = PhotoImage(file="desktop/mysmallcode/1python/pic2.gif")

label1 = Label(window, image=photo1)
label2 = Label(window, image=photo2)

label1.pack(side=LEFT)
label2.pack(side=LEFT)

window.mainloop()
