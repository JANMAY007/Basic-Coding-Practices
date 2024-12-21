from tkinter import *

win = Tk()
# s=Scale(win)
# s.pack()
sb = Spinbox(win, from_=1, to=10)
sb.pack()
scrollbar = Scrollbar(win)
scrollbar.pack(side=RIGHT, fill=Y)
List = Listbox(win, yscrollcommand=scrollbar.set)
for line in range(1, 100):
    List.insert(END, 'This is line no. ' + str(line))
List.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=List.yview)
win.mainloop()
