#wap to take the name of the user and print his short name
'''example:
   i/p Mahesh kumar Singh
   o/p M.K. singh '''

a=str(input("enter the name"))
b=a.split()
c=b[0:len(b)-1]
for i in c:
    print(i[0],".",end="")
print(b[-1])