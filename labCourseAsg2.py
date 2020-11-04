### ATUL RAJARAM PUNDE
### ROLL NO 1655

# Q2    Create a dictionary (in your file) of names and birthdays. 
# When you run your program it should ask the user to enter 
# a name, and return the birthday of that person back to them.

from datetime import date 
import re

bithdate = {}

if __name__ == "__main__":
    while True:
        try:
            print("\n1. Search Birthdate in file")
            print("2. Add Birthdate to file")
            print("3. EXIT")
            ch = int(input("Enter your choice : "))
            if ch<=0:
                print("\nInvalid Input.. Try again..")
                continue

            if ch==1:
                found = False
                search = input("\nEnter name to search = ")
                file = open("D://Sem 4//Python//labCourseAsg2_BirthDate.txt","r") # again open file for reading purpose
                
                tmpList = []

                for i in file.readlines():      # read line by line, we get dictionary with datatype of date 
                    name = i.split(":")[0].split("'")[1]    # so we have to extract the name 
                    bday = i.split(":")[1].split("(")[1].split(")")[0]  # and date
                
                    if search==name:        # if search name is same as extracted name
                        tmpDict = {}        
                        tmpDict[name] = bday    # then create again it to key value pair
                        found = True
                        tmpList.append(tmpDict) # if more record found with same name then add it to dictionary
                if found:
                    print("\nData is found.. ")
                    for i in tmpList:
                        print(i)
                else:
                    print("\nName is not found.")

                file.close()
                ch = input("\nDo you want to continue..? (Y/N) ")
                if ch == "y" or ch=="Y": 
                    continue
                else:
                    break

            if ch==2:
                file = open("D://Sem 4//Python//labCourseAsg2_BirthDate.txt","a") # txt file path..# open file for append

                name = input("Enter name : ")
                if re.search("[a-zA-Z]",name):  # checking validation of name, name should be string only
                    dd = int(input("Day : "))
                    mm = int(input("Month : "))
                    yy = int(input("Year : "))
                    bday = date(yy,mm,dd)   # convert dd,mm,yy in date
                    if bday<date.today():       # birthdate should be less than todays date
                        file.write(str({name:bday}))    # we can not add dictionary to file, so typecast it to string
                        file.write("\n")
                        print("\nData Added Successfully")
                    else:
                        print("\nBirth Date is Greater than todays date.")
                else:
                    print("\nName Not Valid..")
                file.close()
                ch = input("\nDo you want to continue..? (Y/N) ")
                if ch == "y" or ch=="Y": 
                    continue
                else:
                    break

            if ch==3:
                break

        except ValueError as v:
            print("\nError : ",v)
