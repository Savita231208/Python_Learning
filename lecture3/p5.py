#write a program to print sum of digits
num=int(input("enter the number:"))
sum=0
while(num>0):
     dig=num%10
     sum=sum+dig
     num=num//10
print("value of sum is:",sum)
