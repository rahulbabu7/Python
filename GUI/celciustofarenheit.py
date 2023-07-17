from tkinter import *

parent = Tk()  #setting root window where all are mounter



def celTofaren():
    cel = float(myentry2.get())
    faren = cel*1.8+32
    myentry1.set(faren)
    



l1 = Label(parent,text="Farenheit").grid(row=0,column=0)

myentry1 = Entry(parent,font=200)
myentry1.grid(row = 1,column =0)
btn1 = Button(parent,text= ">>>>>").grid(row=2,column=0)

l2 = Label(parent,text="Celcius").grid(row=0,column=3)
myentry2 = Entry(parent,font=200)
myentry2.grid(row = 1,column =3)
btn1 = Button(parent,text= "<<<<<",command=celTofaren).grid(row=2,column=3)

parent.mainloop()



