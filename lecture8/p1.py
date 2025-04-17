#wap to get the second highest number in a list
l=[]
n=int(input("Enter the size:"))
for i in range(0,n):
    a=int(input("Enter the element of the list:"))
    l.append(a)
    print(l)
l.sort()
print("second highest number in the list",l[-2])

