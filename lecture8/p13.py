#Wap to check the occurence of vowels in dictionary
word=input("Enter any word:")
vowels={'a','e','i','o','u'}
d={}
for i in word:
    if i in vowels:
       d[i]=d.get(i,0)+1
for k,v in sorted(d.items()):
     print(k,"occured",v,"times")

