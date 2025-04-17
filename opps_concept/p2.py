class employee:
    def details(self,empid,empname,empsalary):
        self.empid = empid
        self.empname = empname
        self.empsalary = empsalary
    def display(self):
        print("employee id:",self.empid)
        print("employee name:",self.empname)
        print("employee empsalary:",self.empsalary)
e=employee()
eid=int(input("Enter the empid: "))
ename=input("Enter the name: ")
esalary=int(input("Enter the salary: "))    
e.details(eid,ename,esalary)
e.display()      

        