import square
import circle

len = int(input("Input the side of square: "))
print("The area of this square: ", square.area(len), ", ", "the perimeter: ", square.perimeter(len), "\n")

rad = int(input("Input the radius of circle: "))
print("The area of this circle: ", circle.area(rad), ", ", "the perimeter: ", circle.perimeter(rad), "\n")
