#Call by Value and call by reference
def update(lst):
    print(id(lst))
    lst[1]=25
    print("lst",lst)
list=[1,2,3,4]
print(id(list))
update(list)
print("list",list)
