#take a list as an input from user and remove all its duplicates using set().
list=[]
a=int(input("enter the set:"))
for i in range(0,a):
    n=int(input("Enter the list value:"))
    list.append(n)
print(list)
b=set(list)
print(b)
