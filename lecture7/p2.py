'''3 divisible fizz
   5 divisible buzz
   3 & 5 divisible fizz buzz'''
 
for i in range(1,50):
    if(i % 3 and i % 5==0):
       print("fizz buzz")
    elif(i % 3==0):
       print("Fizz")
    elif(i % 5==0):
       print("buzz")
    else:
       print(i)
      
 