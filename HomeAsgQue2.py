# Atul Rajaram Punde
# Roll No 1655

# Q2.	Write a python program to perform CRUD operations 
# on a MySQL Laptop (id, name, price, purchase_date) table 
# using parameterized query. Accept input from user.

import mysql.connector
from datetime import date       # to perform date operation
import re                       # to perform validation of input fields

con = mysql.connector.connect(host="localhost", user="root",passwd="root123") 
cur = con.cursor()                              # Cursor object to perform CRUD operation 

# Custom Exception
class InvalidInputException(Exception):         # inheriting base class - Exception
    def InvalidInputException(self,e):
        super().__init__(e)                     # Invoking base class __init__() method

def ShowDatabase():
    try:
        cur.execute("show databases;")  # Firing query to show databases
        res = cur.fetchall()    # fetching all databases in 'res' object
        if len(res) != 0:
            print(res)      # printing all at a time 
        else:
            print("\nNo any Databases available..")
    except:
        print("Error while fetching database")

def CreateDatabase():
    try:
        cur.execute("create database laptop_database;") # Firing query to create database
        print("\nDatabase Successfully created..")
    except:
        print("\nDatabase already created.")
    
def UseDatabase():
    try:
        cur.execute("use laptop_database;")  # Firing query to use database
        print("\nuse laptop_database;")
        print("\nQuery executed..")
    except:
        print("\nError in Query.")
        print("\nTry Again..")

def ShowTables():
    try:
        cur.execute("show tables;") # Firing query to show tables
        res = cur.fetchall()
        print("")
        if len(res) != 0:
            print(res)
        else:
            print("\nEmpty set\nNo any table available..")
    except:
        print("Invalid Syntax")

def CreateTable():
    try:
        cur.execute("create table Laptop(id varchar(10),name varchar(20),price float,purchase_date date);")  # execute only once
        print("\nNew table created..")  # Firing query to create table.. this is executing only once
    except:
        print("\nLaptop table already Exists.")

def DropTable():
    try:
        cur.execute("drop table Laptop;")   # Firing query to drop the table
        print("\nTable is deleted..")
    except:
        print("\nTable doesn't exist.")
        print("\nTry Again..")
 
def Insert():
    try:
        n = int(input("How Many Records..? "))
        for i in range(n):
            try:
                print("\nFor Record no. ",i+1)
                while True:
                    try:
                        id = input("Enter Laptop Id : ")
                        if len(id)>=4 and re.search("[0-9]",id):      # validation to make Id of length 4 or greater
                            break
                        else:
                            print("\nId should be integer with length greater than four.\n")
                    except ValueError as valueerror:
                        print("\nYour input is invalid.. : ",valueerror)
                        
                while True:
                    name = input("Name : ")
                    if re.search("[0-9]",name):
                        print("\nName is not valid.\n")
                    else:
                        break

                while True:
                    price = input("Price : ")
                    if re.search("[a-zA-Z]",price):
                        print("\nPrice is not valid\n")
                        continue
                    else:
                        break
                    price = float(price)
                while True:
                    try:
                        print("To enter date")
                        while True:
                            dd = input("\tDay : ")
                            if not re.search("[0-9]",dd):
                                print("\nThis day is not valid\n")
                            else:
                                break
                        dd = int(dd)

                        while True:
                            mm = input("\tMonth : ")
                            if not re.search("[0-9]",mm):
                                print("\nThis month is not valid\n")
                            else:
                                break
                        mm = int(mm)

                        while True:
                            yy = input("\tYear : ")
                            if not re.search("[0-9]",yy):
                                print("\nThis year is not valid\n")
                            else:
                                break
                        yy = int(yy)

                        purchase_date = date(yy,mm,dd)  # USE of date() function 
                        if purchase_date > date.today():            # checking validation of date
                            print("\nPurchase date should be less than todays date.\n")
                        else:
                            break
                    except ValueError as v:
                        print("\n",v,"\n")


                try:
                    # Firing query to inserting into table
                    cur.execute("insert into Laptop(id,name,price,purchase_date) values(%s,%s,%s,%s);",(id,name,price,purchase_date))
                    print("\nRecord added successfully.")   
                except:
                    print("\nNo database selected")
                    break
                con.commit()
            except ValueError as valueerror:                
                print("\nYour input is not valid : ",valueerror) 
                print("\nTry Again..")
        
    except ValueError as valueerror:
        print("\nYour input is not valid  : ",valueerror)
        print("\nTry Again..")

def SelectAllFromTable():
    try:
        cur.execute("select * from laptop;")    # Firing query to select all data from table
        res = cur.fetchall()    # fetching all data in 'res' object
        print("\nId\t Name\t\t\t\t Price\t\t Purchace Date")
        for i in res:
            id = i[0]
            name = i[1] 
            name = name+(" "*(16-len(name)))  #Adjustment to align name in tabular form 
            price = i[2]
            purchase_date = i[3]
            print(id,"\t",name,"\t\t",price,"Rs\t",purchase_date)
    except :
        print("\nTable not created Or database not linked.")
 
def DeleteById(delete_id):
    try:
        cur.execute(f"delete from laptop where id='{delete_id}'")   # Firing query to delete row using id
        print("\nRecord permanently deleted from database.")
    except:
        print("\nTable not created Or database not linked.")
    con.commit()

def DeleteByName(delete_name):
    try:
        cur.execute(f"delete from laptop where name='{delete_name}'")   # Firing query to delete using name
        print("\nRecord permanently deleted from database.")
    except:
        print("\nTable not created Or database not linked.")
    con.commit()

def Search(word):
    try:
        cur.execute("select * from laptop;")    # Firing query to select data form table
        res = cur.fetchall()
        flag = True
        for i in res:
            id = i[0]
            name = i[1]  
            price = i[2]
            purchase_date = i[3]
            if word == i[1].strip() or word == id:  ### This is advantage of taking id as string. ###
                print("\nId\t Name\t\t\t Price\t\t Purchace Date")
                print(id,"\t",name,"\t\t",price,"Rs\t",purchase_date)
                flag = False
                break
        if flag == True:
            print(f"\n{word} is not found in database.")
    except :
        print("\nTable not created Or database not linked.")

def UpdateIdBasedOnNames(id,name):
    try:
        cur.execute("update laptop set id = %s where name = %s",(id,name))  # Firing query to update Id
        print("\nLaptop Id updated..")
    except:
        print("\nTable not created Or database not linked.")
    con.commit()

def UpdateNameBasedOnId(name,id):
    try:
        cur.execute("update laptop set name = %s where id = %s",(name,id))  # Firing query to update name
        print("\nLaptop name updated..")
    except:
        print("\nTable not created Or database not linked.")
    con.commit()

def isContinue():   # to reduce code 
    choice = input("\nDo you want to continue..? (Y/N) ")
    if choice == 'y' or choice == 'Y':
        return True
    else:
        return False

if __name__ == "__main__":
    
    flag = True
    while flag:
        try:
            print("\n**** Main Menu ****")
            print("\n1. Show databases;")
            print("2. create  database laptop_database;")
            print("3. use laptop_database;")
            print("4. show tables;")
            print("5. Create New Table Laptop")
            print("6. drop table Laptop;")
            print("7. Insert")
            print("8. Update")
            print("9. Delete")
            print("10. Search")
            print("11. Select * from Laptop;")
            print("12. EXIT") 
            ch = int(input("Enter your choice : "))

            if ch==1:
                ShowDatabase()
                if isContinue():
                    continue
                else:
                    break
            if ch==2:
                CreateDatabase()
                if isContinue():
                    continue
                else:
                    break
            if ch==3:
                UseDatabase()
                if isContinue():
                    continue
                else:
                    break
            if ch==4:
                ShowTables()
                if isContinue():
                    continue
                else:
                    break
            if ch==5:
                CreateTable()
                if isContinue():
                    continue
                else:
                    break
            if ch==6:
                ch6 = input("\nAre you sure.?\nDo you want to delete table..? (Y/N) ")
                if ch6=='y' or ch6=='Y':
                    DropTable()
                else:
                    print("\nTable is as it is.")
                if isContinue():
                    continue
                else:
                    break

            if ch==7:
                Insert()
                if isContinue():
                    continue
                else:
                    break

            if ch==8:
                while True:
                    try:
                        print("\n\t1. Update Id's based on names")
                        print("\t2. Update name's based on Id")
                        print("\t3. Previous Menu")
                        ch3 = int(input("\tENter your choice : "))
                        if ch3==1:
                            while True:
                                try:
                                    id = input("update laptop set id = ")
                                    if len(id)>=4 and re.search("[0-9]",id):      # validation to make Id of length 4 or greater
                                        break
                                    else:
                                        print("\nId should be integer with length greater than four.\n")
                                except ValueError as valueerror:
                                    print("\nYour input is invalid.. : ",valueerror)
                            
                            while True:
                                name = input("where name = ")
                                if re.search("[0-9]",name):
                                    print("\nName is not valid.\n")
                                else:
                                    break
                            UpdateIdBasedOnNames(id,name)
                            continue
                        if ch3==2:
                            while True:
                                name = input("update laptop set name = ")
                                if re.search("[0-9]",name):
                                    print("\nName is not valid.\n")
                                else:
                                    break
                            while True:
                                try:
                                    id = input("where id = ")
                                    if len(id)>=4 and re.search("[0-9]",id):      # validation to make Id of length 4 or greater
                                        break
                                    else:
                                        print("\nId should be integer with length greater than four.\n")
                                except ValueError as valueerror:
                                    print("\nYour input is invalid.. : ",valueerror)
                            UpdateNameBasedOnId(name,id)
                            continue
                        if ch3==3:
                            break
                        if ch3<=0 or ch3>=4:
                            raise InvalidInputException("Your choice is wrong..")

                    except ValueError as valErr:
                            print("\nYour input is not valid : ",valueerror)
                            print("\nTry Again..")
                    except InvalidInputException as iie:
                        print(iie,ch3)
                if isContinue():
                    continue

                else:
                    break

            if ch==9:
                while True:
                    print("\n\t1. Delete by Id")
                    print("\t2. Delete by Name")
                    print("\t3. Previous Menu")
                    ch4 = int(input("Enter your choice : "))

                    if ch4==1:
                        while True:
                            try:
                                id = input("Enter Id to delete record : ")
                                if len(id)>=4 and re.search("[0-9]",id):      # validation to make Id of length 4 or greater
                                    break
                                else:
                                    print("\nId should be integer with length greater than four.\n")
                            except ValueError as valueerror:
                                print("\nYour input is invalid.. : ",valueerror)
                        DeleteById(id)
                        continue
                    if ch4==2:
                        while True:
                                    delete_name = input("\n\tEnter Name to delete record : ")
                                    if re.search("[0-9]",delete_name):
                                        print("\nName is not valid.\n")
                                    else:
                                        break
                        
                        DeleteByName(delete_name)
                        continue
                    if ch4==3:
                        break
                    if ch4>=4:
                        raise InvalidInputException("\nYour choice is wrong..")
                        continue                   
                if isContinue():
                    continue
                else:
                    break

            if ch==10:
                search = input("Enter Id Or name to search : ")
                Search(search)
                if isContinue():
                    continue
                else:
                    break

            if ch==11:
                SelectAllFromTable()
                continue

            if ch==12:
                break

            if ch<=0 or ch>=13:
                raise InvalidInputException("\nYour choice is wrong..")
                
        except ValueError as valueerror:
            print("\nYour Input is not valid : ",valueerror)
            print("\nTry Again..")
        except InvalidInputException as iie:
            print(iie,ch)

con.close()     # closing connection
print("\nConnection is closed..\n")