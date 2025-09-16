"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    # Method to get the area
    def get_area(self):
        area = self.__length * self.__width
        return f"area = {area}" 

    # Method to get the perimeter
    def get_perimeter(self):
        perimeter = (self.__length + self.__width) * 2
        print("perimeter = " + perimeter)
    
    def isSquare(self):
        if self.__length == self.__width:
            return True
        else:
            return False
        
myRectangle = Rectangle(10,2)
print("Rectangle Area:", myRectangle.get_area()) 
myRectangle.get_perimeter()       
print("Rectangle Perimeter:", myRectangle.get_perimeter())
