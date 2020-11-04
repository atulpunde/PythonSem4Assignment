# Atul Rajaram Punde
# Roll No 1655

# Q3.	Write a python program to create two Python list.
# Iterate both lists simultaneously such that list1 should display
# item in original order and list2 in reverse order.

while True:
    list1 = []
    list2 = []
    try:
        n = int(input("Enter Number Of Elements : "))

        print("\nEnter Element in First List : ")
        for i in range(n):
            print(f"Enter element {i+1} = ",end="")
            list1.append(input())               # input may be int or string

        print("\nEnter Element in Second List : ")
        for i in range(n):
            print(f"Enter element {i+1} = ",end="")
            list2.append(input())

        print("\nThere are many ways to iterate multiple lists simultaneously using single for loop..\n")
        print("\nPrinting Both Lists using simple method")
        print("List 1\t\tList 2")
        for i in range(n):
            print(list1[i],end="\t\t")
            print(list2[::-1][i])       ## printing list2 in reverse order using same variable (i)

        print("\nPrinting Both Lists using zip function")
        print("List 1\t\tList 2")
        for i,j in zip(list1,list2[::-1]):
            print(i,end="\t\t")
            print(j)       
    except ValueError as v:
        print("\nYour input is invalid : ",v)

    ch = input("\nDo you want to continue.? (Y/N) ")        # menu driven
    if ch=="y" or ch=="Y":
        continue
    else:
        break