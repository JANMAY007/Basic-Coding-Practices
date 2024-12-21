from tkinter import *

win = Tk()
mb = Menubutton(win, text='file')
mb.grid()
mb.menu = Menu(mb)
mb['menu'] = mb.menu
x1 = IntVar()
x2 = IntVar()
mb.menu.add_radiobutton(label='open', variable='x1')
mb.menu.add_radiobutton(label='close', variable='x2')
mb.pack()
win.mainloop()
win1 = Tk()


def nothing():
    file = Toplevel(win)
    button = Button(file, text='do nothing')
    button.pack()


menubar = Menu(win1)
filemenu = Menu(menubar)
filemenu.add_command(label='open', command=nothing)
filemenu.add_separator()
filemenu.add_command(label='new file', command=nothing)
filemenu.add_command(label='save', command=nothing)
filemenu.add_command(label='save as', command=nothing)
filemenu.add_separator()
filemenu.add_command(label='close', command=win.quit)
menubar.add_cascade(label='File', menu=filemenu)
win1.config(menu=menubar)
win.mainloop()
