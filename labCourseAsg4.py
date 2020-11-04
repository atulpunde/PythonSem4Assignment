### ATUL RAJARAM PUNDE
### ROLL NO 1655

# Q4 Write a python program to create the following GUI for user registration form. 
# Accept Full Name, Contact Number and Email Id from the user and s store it into database and print it.

from tkinter import *
import tkinter.messagebox
import re
import mysql.connector

window = Tk()       # creating top level window
window.geometry("700x700")
window.title("Registration Form")   # to add title

canvas = Canvas(window,bg="light yellow",heigh=320,width=420) # add canvas to provide better look
canvas.place(x=60,y=5)

heading = Label(window,text="Registration Form",font=("Calibri",24,"bold","underline"),fg="red")
heading.place(x=140,y=20)

fname = Label(window,text="Full Name : ",font=("Arial",14,"bold"),fg="green",padx=6)
fname.place(x=90,y=80)
fullName = Entry(window,font=("Arial",14))      #accepting full name
fullName.place(x=220,y=84)

contactNo = Label(window,text="Contact No : ",font=("Arial",14,"bold"),fg="green")
contactNo.place(x=90,y=140)
mobNo = Entry(window,font=("Arial",14))         # accepting mobile number
mobNo.place(x=220,y=144)

emailId = Label(window,text="Email Id : ",font=("Arial",14,"bold"),fg="green",padx=15)
emailId.place(x=90,y=200)
email = Entry(window,font=("Arial",14))     # accepting email
email.place(x=220,y=204)

def AddToDB():
    fName = (fullName.get()).strip()    # to check validation, copy into another variable
    mobile = (mobNo.get()).strip()
    mail = (email.get()).strip()

    f1,f2,f3=True,True,True     #flag to check validity of first name, mobile, email
    if fName=="" or re.search("[0-9]",fName)  or len(fName)<=1:     # check first name validation
        tkinter.messagebox.showerror("Full Name Error","Full Name is Invalid..")
        fullName.delete(0,END)
        f1=False
    if mobile=="" or not re.search("[0-9]",mobile) or (len(mobile)!=10):        # check mobile number validation
        tkinter.messagebox.showerror("Mobile Number Error","Mobile number is Invalid..")
        mobNo.delete(0,END)
        f2=False
    if mail=="" or '@' not in mail or '.' not in mail or len(mail)<8:       # check mail validation
        tkinter.messagebox.showerror("Email Error","Email is Invalid..")
        email.delete(0,END)
        f3=False
    
    if f1 and f2 and f3:
        print("\nUser Details : ")
        print("First Name : ",fName)        # printing data on console
        print("Mobile No  : ",mobile)
        print("Email Id   : ",mail)

        try:                    # make database connectivity 
            con = mysql.connector.connect(host="localhost",user="root",passwd="root123")
            cur = con.cursor()
            # cur.execute("drop database registeruser;")        ### YOU CAN UNCOMMENT CODE, IF REQUIRED
            # cur.execute("create database registeruser;")
            cur.execute("use registeruser;")
            # cur.execute("drop table register;")
            # cur.execute("create table register(FirstName varchar(20),mobileNo varchar(10),emailId varchar(20));")
            cur.execute("insert into register(FirstName,mobileNo,emailId) values(%s,%s,%s)",(fName,mobile,mail))
            con.commit()
            con.close()
        except:
            print("Error in database operation..")
        print("\nRegistration Successful..")

        print("Data Successfully Stored..")
        tkinter.messagebox.showinfo("Information","Data Successfully Stored..")
        fullName.delete(0,END)      # after registering user make input fields empty for another user
        mobNo.delete(0,END)
        email.delete(0,END)

submit = Button(window,font=("Arial",14,"bold"),text="Submit",bg="Blue",padx=10,fg="white",command=AddToDB)
submit.place(x=200,y=260)

window.mainloop()
