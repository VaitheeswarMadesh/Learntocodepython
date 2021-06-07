class employee:   #class creating
    def __init__(self,eid,name,salary):   #attributes/ properties creation
        self.eid=eid
        self.name=name
        self.salary=salary

class student(employee):  #inherit
    def __init__(self,eid,name,salary, fathername, mothername): 
        employee.__init__(self,eid,name,salary) #calling superclass
        self.fathername = fathername
        self.mothername = mothername

a = student(69,"Mike",75875,"John","Mary")
print(a.name, a.eid)

