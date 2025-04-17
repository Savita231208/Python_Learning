#Write a python program to create two functions area() and peri() to find area and perimeter of rectangle.
def area(l,b):
    result=l*b
    return result
def perimeter(l,b):
    result=2*(l+b)
    return result
a=5
b=6
ar=area(a,b)
peri=perimeter(a,b)
print("area:",ar)
print("perimeter:",peri)
    