## PASSWORD GENERATOR APP ##

from tkinter import *
import random
import string

# Creating functions
def generate_password():
    password = passgen()
    lsum.config(text=password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance, val.get()))

def copy_to_clipboard():
    generated_password = password_entry.get()
    root.clipboard_clear()
    root.clipboard_append(generated_password)
    root.update()
    copy_status.config(text="Text copied!")

# Main Window
root = Tk()
root.geometry("525x325")  
root.title("Password Generator APP")

title = StringVar()
label = Label(root, textvariable=title)
label.pack()
title.set("PASSWORD GENERATOR")

choice = IntVar()
R1 = Radiobutton(root, text="WEAK", variable=choice, value=1)
R2 = Radiobutton(root, text="AVERAGE", variable=choice, value=2)
R3 = Radiobutton(root, text="STRONG", variable=choice, value=3)
R1.pack(anchor=CENTER)
R2.pack(anchor=CENTER)
R3.pack(anchor=CENTER)

lenlabel = StringVar()
lenlabel.set("Password length:")
lentitle = Label(root, textvariable=lenlabel)
lentitle.pack()

val = IntVar()
spinlength = Spinbox(root, from_=4, to_=24, textvariable=val, width=13)
spinlength.pack()

password_entry = Entry(root) 
password_entry.pack()

passgenButton = Button(root, text="Generate Password", bd=5, command=generate_password)
passgenButton.pack(pady=20)

copy_button = Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

lsum = Label(root, text="Password here", font=("arial", 15))
lsum.pack(side=TOP, anchor="n")

copy_status = Label(root, text="", fg="green")
copy_status.pack()

poor = string.ascii_lowercase
average = string.ascii_letters + string.digits
advance = string.ascii_letters + string.digits + string.punctuation

root.mainloop()
