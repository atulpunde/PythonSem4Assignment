from threading import *

class FileOperations(object):
    def Write(self,data):
        try:
            print("Writing in a File")
            file=open("D://Sem 4//Python//Assignments Lockdown//test.txt","w")
            file.write(data)
            print("Closiing the operation of Writing in a file")
            file.close()
            print("Successfully Written")
        except:
            print("Error occured while writing in a file")
    def Read(self):
        try:
            print("Reading of a file")
            file=open("D://Sem 4//Python//Assignments Lockdown//test.txt","r")
            for i in file:
                print("The contents of the file are:",i)
            print("Closing the file")
            file.close()
            print("Successfully Read")
        except:
            print("Error while reading the file")

if __name__ =="__main__":
    try:
        file=FileOperations() #Creating Object  of the class
        data=input("Enter the item to read or write in a file :")
        t1 =Thread(target=file.Write(data)) 
        t2 =Thread(target=file.Read())
        t1.start()
        t2.start()
    except:
        print("Error Occured in file") 