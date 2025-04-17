# Wap to check palindrom number
num=int(input("Enter the number:"))
reverse=0
temp=num
while(num>0):
      remainder=num%10
      reverse=(reverse*10)+remainder
      num=num//10
if(temp==reverse):
   print("palindrom number")
else:
   print("not a palindrom number")