from tkinter import *
root = Tk()

title = root.title("SignUP")

def check():
    if myentry3.get() == myentry4.get():
        print("Sign up successful")
    else:
        print("Passwords mismatch")

l1 = Label(root, text="SignUP", font=100).grid(row=0, column=0)

l2 = Label(root, text="Name").grid(row=2, column=1)
myentry1 = Entry(root)
myentry1.grid(row=2, column=2)
myentry1.insert(0, "Enter name")  # Placeholder for name field

l3 = Label(root, text="Password").grid(row=4, column=1)
myentry3 = Entry(root, show="*")
myentry3.grid(row=4, column=2)
myentry3.insert(0, "Enter password")  # Placeholder for password field

l4 = Label(root, text="Confirm Password").grid(row=6, column=1)
myentry4 = Entry(root, show="*")
myentry4.grid(row=6, column=2)
myentry4.insert(0, "Confirm password")  # Placeholder for confirm password field

submit = Button(root, text="Submit", command=check).grid(row=7, column=2)
root.mainloop()
