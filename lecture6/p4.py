#replace() function
#wap india is a great country
#replace great==best
n=str(input("enter the string:"))
a="great"
for i in n:
    if(i==a):
       n2=n.replace("great","best")
       print(n2)
    else:
        print(n)




