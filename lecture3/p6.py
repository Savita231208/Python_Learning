#write a program to get the reverse of digits of a number
num=int(input("Enter the number:"))
reverse=0
while(num>0):
      remainder=num%10
      reverse=(reverse*10)+remainder
      num=num//10
print("reverse of the number:",reverse)