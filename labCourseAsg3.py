### ATUL RAJARAM PUNDE
### ROLL NO 1655

# Q3    Write a Python class named Circle constructed by a radius 
# and two methods which will compute the area and the perimeter of a circle

from math import pi     # we are importing only pi from math module

class Circle(object):
    ''' Method to calculate area of circle '''
    def Area(self,radius):
        return pi*radius**2     # return ans by calculating it

    ''' Method to calculate Perimeter of circle '''
    def Perimeter(self,radius):
        return 2*pi*radius      # calculate and return it

if __name__ == "__main__":
    while True:
        try:
            print("\n----- CALCULATOR -----")
            print("1. Area of Circle")
            print("2. Perimeter of Circle")
            print("3. EXIT")
            ch = int(input("Enter your choice : "))
            if ch<=0:
                print("\nInvalid input..Try again..")
                continue

            circle = Circle()           # To access methods create object of class 

            if ch==1:
                radius = float(input("\nEnter radius of circle = "))
                if radius<0:
                    print("\nRadius is not valid..Try again..")
                    continue
                area = circle.Area(radius)  # pass Area() radius, we get area
                print(f"Area of circle having radius {radius} is {round(area,4)} square unit")# printing answer with UNIT

            if ch==2:
                radius = float(input("\nEnter radius of circle = "))
                if radius<0:
                    print("\nRadius is not valid..Try again..")
                    continue
                perimeter = circle.Perimeter(radius)
                print(f"Perimeter of circle having radius {radius} is {round(perimeter,4)} unit")# printing answer with UNIT

            if ch==3:
                break

            if ch>=4:
                print("Enter proper choice.")

        except ValueError as v:
            print("\nError : ",v)
