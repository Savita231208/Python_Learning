# take sentence as input,now count the occurence of word "The"
a=str(input("enter a string"))
b=a.split()
count=0
for i in b:
    if(i=='the'):
       count=count+1
    else:
         pass
print(count)
