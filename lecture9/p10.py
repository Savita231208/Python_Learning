#Pass a list in a function and count the even and odd inside that list
def count(ls):
    even=0
    odd=0
    for i in ls:
        if(i%2==0):
           even= even+1
        else:
           odd= odd+1
    return even,odd
lst=[10,20,13,17,16]
e,o=count(lst)
print("even inside a list:",e)
print("odd inside a list:",o)
    
      