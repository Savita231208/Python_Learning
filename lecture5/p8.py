#wap to take input from user and display in ascending order
n=int(input("please tell how many items you want to put"))
l=[]
for i in range (5):
    n1=input()
    l.append(n1)
l.sort()
a=max
b=min(l)
for i in l:
    print(i)
