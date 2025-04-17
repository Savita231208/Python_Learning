#wap to take input from user and remove all the duplicates
#example:
#str="aaabcdbcd"
str=str(input("Enter the string"))
blank_string=""
for i in str:
    if i in blank_string:
       pass
    else:
         blank_string=blank_string+i
print(blank_string)