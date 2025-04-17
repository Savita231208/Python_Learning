#WAP in python to find volume of cuboid using user defined function
def cuboid(l,b,h):
   result=l*b*h
   return result
a=int(input("Enter  the value of length:"))
b=int(input("Enter  the value of breadth:"))
c=int(input("Enter  the value of height:"))
volume=cuboid(a,b,c)
print(volume)