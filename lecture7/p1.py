#compress the string
input="aaaabbbccccddkmmmmm"
#new_str="a4b3c4d2k1m5"
blank_string=""
for i in input:
    count=0
    if i not in blank_string:
           for j in input:
               if(i==j):
                 count=count+1
           if(count!=0):
             blank_string=blank_string+i+str(count)
print(blank_string)


     
