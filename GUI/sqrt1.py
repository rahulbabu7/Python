from tkinter import *
import  math
parent = Tk()


title = parent.title("Converter")
def sqr():
    num = int(e1.get())
    result = round(math.sqrt(num),2)
    e2.insert(0,result)



l1 = Label(parent,text="Enter the number").grid(row=0,column=0)
e1 = Entry(parent)
e1.grid(row=0,column= 1)
l2 = Label(parent,text="result").grid(row=1,column=0)
e2 = Entry(parent)
e2.grid(row=1,column= 1)
btn = Button(parent,text = "Convert",command = sqr).grid(row = 2,column = 1)

parent.mainloop()