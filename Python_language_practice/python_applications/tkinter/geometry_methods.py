from tkinter import *

win1 = Tk()
b = 0
for i in range(6):
    for j in range(6):
        b = b + 1
        Button(win1, text=str(b), borderwidth=1).grid(row=i, column=j)
win1.mainloop()
win2 = Tk()
l1 = Label(win2, text='Maths')
l1.place(x=10, y=10)
e1 = Entry(win2)
e1.place(x=60, y=10)
l2 = Label(win2, text='Sanskrut')
l2.place(x=10, y=60)
e2 = Entry(win2)
e2.place(x=60, y=60)
button = Button(win2, text='submit')
button.place(x=100, y=100)
win2.mainloop()
