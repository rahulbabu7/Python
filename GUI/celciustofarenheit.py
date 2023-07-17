from tkinter import *

parent = Tk()  #setting root window where all are mounter

title = parent.title("TempConvereter")

def celTofaren():
    cel = float(myentry2.get())
    faren = cel*1.8+32
    myentry1.insert(0, faren)

def farenTocel():
    faren = float(myentry1.get())
    cel = (faren-32)/1.8
    myentry2.insert(0, cel)
    
    



l1 = Label(parent,text="Farenheit").grid(row=0,column=0)

myentry1 = Entry(parent,font=200)
myentry1.grid(row = 1,column =0)
myentry1.insert(0,32)
btn1 = Button(parent,text= ">>>>>",command = farenTocel).grid(row=2,column=0)

l2 = Label(parent,text="Celcius").grid(row=0,column=3)
myentry2 = Entry(parent,font=200)
myentry2.grid(row = 1,column =3)
myentry2.insert(0,0)
btn1 = Button(parent,text= "<<<<<",command=celTofaren).grid(row=2,column=3)

parent.mainloop()



