#Marco Villegas
#5/22/23

#Problem 1
print("\n\nProgram 1 - AreaOfCircle.py")
import math
radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius**2 

print("Area of the circle is: {0}".format(area))

#Problem 2
print("\n\nProgram 2 - CheckRange.py")
def test_range(n):
    if n in range(1,10):
        print(" %s is in the range"%str(n))
    else :
        print("The number is outside the given range")
test_range(8)



#Problem 3
print("\n\nProgram 3 - MultiplyList.py")
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print("The final result after  multiplying the list is: ", multiply((5, 2, 7, -1)))



#Problem 4
print("\n\nProgram 4 - Unique.py")
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print("After appending 3 you will get a unique list of: ", unique_list([1,3,3,3,6,2,3,5])) 



#Problem 5
print("\n\nProgram 5 - Squares.py")
from turtle import *
print("Multiple squares will be drawn!")
def draw_square(a,color,x,y):
    penup()
    goto(x,y)
    setheading(90)
    backward(a//2)
    setheading(0)
    backward(a//2)
    pendown()
    pencolor(color)
    for _ in range(4):
        forward(a)
        left(90)

draw_square(20,"blue",0,0)
draw_square(40,"blue",0,0)
draw_square(60,"blue",0,0)
draw_square(80,"blue",0,0)
draw_square(100,"blue",0,0)




#Problem 6
print("\n\nProgram 6 - Flower.py")
from turtle import *
print("The pink flower will be drawn!")
for i in range(10):
    pencolor("pink")
    pensize(3)
    for p in range(6):
        left(60)
        forward(100)
    left(36)
ht()
exitonclick()

