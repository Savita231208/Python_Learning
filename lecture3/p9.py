# Wap to check Armstrong number or not
num=int(input("Enter the number:"))
sum=0
temp=num
while(temp>0):
      digit=temp%10
      sum=sum+digit*digit*digit
      temp=temp//10
if(sum==num):
   print("Armstrong number")
else:
   print("not an armstrong number")