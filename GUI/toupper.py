from tkinter import *

parent = Tk()

title = parent.title("TO upper")


def convert():
    text = entry1.get()
    result = text.upper()
    entry2.insert(0,result)

l1 = Label(parent,text="input").grid(row=0,column = 0)
entry1 = Entry(parent)
entry1.grid(row = 0,column = 1)
l2 = Label(parent,text="output").grid(row=1,column = 0)
entry2 = Entry(parent)
entry2.grid(row = 1,column = 1)
btn = Button(parent,text = "convert",command = convert).grid(row =3,column = 1)
parent.mainloop()