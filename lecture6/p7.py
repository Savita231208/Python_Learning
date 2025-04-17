#wap to take string from user and check weather it is a pelindrom or not
a=str(input("enter a string:"))
reverse=a[: : -1]
print(reverse)
if(a==reverse):
   print("it is palindrom")
else:
   print("it is not palindrom")
