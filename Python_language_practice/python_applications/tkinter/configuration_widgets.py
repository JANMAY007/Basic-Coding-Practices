from tkinter import *
from tkinter import messagebox

win1 = Tk()
frame1 = Frame(win1)
# buttons
frame1.pack()
frame2 = Frame(win1)
frame2.pack(side=BOTTOM)
rb = Button(frame1, text='Red', fg='red')
rb.pack(side=LEFT)
bb = Button(frame1, text='Blue', fg='Blue')
bb.pack(side=LEFT)
blb = Button(frame1, text='Black', fg='Black')
blb.pack(side=LEFT)
gb = Button(frame2, text='Red', fg='red')
gb.pack(side=BOTTOM)
# listbox
lb = Listbox(win1)
lb.insert(1, 'python')
lb.insert(2, 'c')
lb.insert(3, 'c++')
lb.insert(4, 'ruby')
lb.insert(5, 'swift')
lb.pack()


# message box
def hello():
    messagebox.showinfo('from computer', 'hey there')


b = Button(win1, text='popup', command=hello)
b.pack()
win1.mainloop()
win2 = Tk()
# top window
win2.title('first')
top = Toplevel()
top.title('second')
win2.mainloop()
