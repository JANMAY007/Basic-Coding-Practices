from tkinter import *

# any thing written in between TK() and mainloop() will work in the formed window
win = Tk()
win.geometry("400x400")
# b1=Button(win,text='Button1')
# b1.pack()
b2 = Button(win, text='Button2')
b2.grid(row=2, column=1)
b3 = Button(win, text='Button3')
b3.place(x=300, y=300)
win.mainloop()
