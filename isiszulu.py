from tkinter import *
from datetime import date

root = Tk()
root.title("Getting started with Widgets")
root.geometry('400x300')

lbl = Label(text="hey There!", fg="white", bg="#072F5F", height=1, width=300)

name_lbl = Label(text="Full Name", bg="#3895D3")
name_entry = Entry()

def display():
    name = name_entry.get()

    global Message
    message = "Welcome to the Application! \nToday's date is: "
    greeet = "Hello "+name+"\n"

    text_box.insert(END, greeet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

text_box = Text(height=3)

btn = Button(text="Begin", command=display, height=1, fg='white', bg="#1261A0")

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop()