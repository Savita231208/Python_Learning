# wap to take input name and % of marks of students in a dictionary and display the information
d={}
n=int(input("Enter the number of students:"))
i=1
while i<=n:
    name=input("Enter student name:")
    marks=input("Enter % of marks of student:")
    d[name]=marks
    i=i+1
for x in d:
    print(x,d[x])