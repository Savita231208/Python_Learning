#check that any number is an armstrong number or not
num=int(input("Enter a number:"))
sum=0
temp=num
while(temp>0):
       digit=temp%10
       sum=sum+digit**3
       temp=temp//10
if num==sum:
   print("Armstrong number")
else:
   print("not an armstrong number")