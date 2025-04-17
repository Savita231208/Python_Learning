#Wap to take tuple of numbers from keywords and perform sum and avg.
a=eval(input("Enter the tuple"))
length=len(a)
sum=0
for i in a:
    sum=sum+i
    avg=sum/length
print("sum is:",sum)
print("average is:",avg)
    
