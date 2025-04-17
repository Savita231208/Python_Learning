#Wap to check the number of occurence of each character #present in a string

word=input("Enter any word:")
d={}
for i in word:
    d[i]=d.get(i,0)+1
for k,v in d.items():
     print(k,"occured",v,"times")


