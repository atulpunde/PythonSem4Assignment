# Atul Rajaram Punde
# Roll No 1655

# Q1.   Write a python program to generate a random Password which meets the following conditions:
# •	Password length must be 10 characters long.
# •	It must contain at least 2 upper case letters, 1 digit, and 1 special symbol. 
# [Hint: Use string and random modules]

# Making GUI is not mention in the question, but program is so simple so I used GUI.

from tkinter import *
import random

def DisplayPassword():
    f = True
    while f:            # If Password is invalid, Repeat till we get valid password
        password = " "
        upperCase=0
        digitCount=0
        specialCharCount=0
        for i in range(10):
            password+=random.choice(MixString) # Generating random password of length 10 
        
        for i in password:
            if i.isupper():
                upperCase = upperCase+1     # It checks validity of password
            if i.isdigit():
                digitCount = digitCount+1
            else:
                specialCharCount = specialCharCount+1
        if upperCase>=2 and digitCount>=1 and specialCharCount>=1: # If we got required validation 
            lb.delete(0)
            lb.insert(END,password)           # insert into listbox to show user
            f=False
        else:
            f=True

window = Tk()           # to open top window
window.geometry("700x500")

canvas =Canvas(window,bg="light blue",height=280,width=550)
canvas.place(x=10,y=30)

rpg = Label(text="Random Password Generator",font=("Arial",20,"bold","underline"))
rpg.place(x=80,y=60)

pswd = Label(text="Password : ",fg="blue",font=("Arial",16))
pswd.place(x=45,y=170)

lb = Listbox(window,font=("Arial"),height=1,width=30)
lb.place(x=180,y=170)

# as mention in question (uppercase + digits + special character) + lowercase
MixString = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*abcdefghijklmnopqrstuvwxyz"      

# you can click this button many times to generate new password every time
b = Button(text="Generate Password",fg="white",font=("Arial",16,"bold"),bg="green",command=DisplayPassword)
b.place(x=180,y=240)

# this is another canvas to show validation of program
canvas =Canvas(window,bg="light green",height=100,width=550)
canvas.place(x=10,y=350)

condition = Label(window,text="CONDITIONS:")
condition.place(x=40,y=360)
label1 = Label(window,text="•    Password length must be 10 characters long.")
label1.place(x=40,y=390)
label2 = Label(window,text="•   It must contain at least 2 upper case letters, 1 digit, and 1 special symbol. ")
label2.place(x=40,y=420)

window.mainloop()