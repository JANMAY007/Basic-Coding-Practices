from tkinter import *
from functools import partial

win = Tk()


def Sum(label, x1, x2):
    n1 = (x1.get())
    n2 = (x2.get())
    sum = int(n1) + int(n2)
    label.config(text='sum is %d' % sum)
    return label


l1 = Label(win, text='first number')
l1.grid(row=1, column=0)
l2 = Label(win, text='second number')
l2.grid(row=2, column=0)
x1 = IntVar()
x2 = IntVar()
e1 = Entry(win, textvariable=x1)
e1.grid(row=1, column=1)
e2 = Entry(win, textvariable=x2)
e2.grid(row=2, column=1)
l = Label(win)
l.grid(row=3, column=1)
Sum = partial(Sum, l, x1, x2)
b = Button(win, text='calculate', command=Sum)
b.grid(row=3, column=0)
win.mainloop()
