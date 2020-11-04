### ATUL RAJARAM PUNDE
### ROLL NO 1655

# Q1    Write a program that returns a list that contains 
# only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.

def CheckCommons():
    return [i for i in list1 if i in list2] # copy if elements are common in both list

if __name__ == "__main__":    
    flag=True
    while flag:
        list1,list2,list3 = [],[],[]    # to avoid complexity create new list everytime
        try:
            n1 = int(input("Enter number of element in first list = "))
            if n1<=0:
                print("Invalid Input.")
                continue
            n2 = int(input("Enter number of element in second list = "))
            if n2<=0:
                print("Invalid Input.")
                continue
            print("\nEnter element in first list : ")
            for i in range(n1):
                print(f"list1[{i}] = ",end="")
                list1.append(input())    # you can append int or float or str

            print("\nEnter element in second list : ")
            for i in range(n2):
                print(f"list2[{i}] = ",end="")
                list2.append(input())    # you can append int or float or str

            if len(set(CheckCommons()))!=0:
                print("\nCommon elements are : ",set(CheckCommons()))   # ignored duplicates
            else:
                print("No common elements in list1 and list2.")
        except ValueError as v:
            print("\nError : ",v)

        ch = input("\nDo you want to continue..? (Y/N) ")
        if ch == "y" or ch=="Y": 
            flag=True
        else:
            flag=False
