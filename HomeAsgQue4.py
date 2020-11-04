# Atul Rajaram Punde
# Roll No 1655

# Q4.   Write a python program to create a thread and perform 
# read and write operations on file using these threads.

from threading import *

class FileOperation(object):
    def Write(self,data):
        try:
            print("\nWriting into file..")
            file = open("Test1","w")     # Open file for writing purpose
            file.write(data)             # Writing data into file
            file.close()             # File is closed.
            print("\nFile writing is closed..")
        except:
            print("Problem while Writing into the file..")

    def Read(self):
        try:
            print("\nReading from file..")
            file = open("Test1","r")
            for i in file:              # Reading from file 
                print(i)
            file.close()
            print("\nFile reading is closed..\n")
        except:
            print("Problem while Reading the file..")

if __name__ == "__main__":
    try:
        file = FileOperation()  # Creating object of class 

        data = input("Enter data to write in file : ") # Accepting data from user

        thread1 = Thread(target=file.Write(data))   #one way to create thread for writing purpose
        thread2 = Thread(target=file.Read())    # create thread for Reading purpose

        thread1.start()         # Starting both thread
        thread2.start()
    except:
        print("Problem in Creating thread..")