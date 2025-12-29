# Area and perimeter of a rectangle

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print("The area of a rectangle is " + str(area) +
      " and the perimeter is " + str(perimeter))
