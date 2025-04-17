class A:
    def feature1(self):
        print("you are inside the class A and fearure1")
    def feature2(self):
        print("you are inside the class A and feature2")
class B(A):
    def feature3(self):
        print("you are inside the class B and feature3")
    def feature4(self):
        print("you are inside the class B and feature4")
a=A()
a.feature1()
b=B()
b.feature3()
b.feature1()
    