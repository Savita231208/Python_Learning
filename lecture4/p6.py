# print prime number from 10 t0 50
n1=int(input("Enter range:"))
n2=int(input("Enter range:"))
for i in range(n1,n2):
    for k in range(2,i): 
        if(i%k==0):
           break
    else:
         print(i)  