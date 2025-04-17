#Wap to make a simple calculator using defined function
def calculator(x,y):
    c=x+y
    d=x-y
    e=x*y
    f=x/y
    return c,d,e,f
a=int(input("enter the value:"))
b=int(input("Enter the value:"))
sum,sub,mul,div=calculator(a,b)
print("sum:",sum)
print("subtractin:",sub)
print("multiplication:",mul)
print("Division:",div)