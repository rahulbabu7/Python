from tkinter import *
top = Tk()
top.geometry("200x200")

chkbtn1 = Checkbutton(top, text="C", height=2, width=10)
chkbtn2 = Checkbutton(top, text="C++")
chkbtn3 = Checkbutton(top, text="Java")
chkbtn1.pack()
chkbtn2.pack()
chkbtn3.pack()
top.mainloop()
