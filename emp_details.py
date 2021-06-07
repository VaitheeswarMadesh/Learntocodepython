class employee:   #class creating
    def __init__(self,eid,name,salary):   #attributes/ properties creation
        self.eid=eid
        self.name=name
        self.salary=salary

a=employee("87u982", "Mike", "98712419")   #creating a object
print(a.eid, a.salary)

x="Loop Succesful"
for i in a.eid:
    print(x)
if int(a.salary)>10000000000:
    print("YOU ARE A MILLIONIARE")
else:
    print("You are still a millionaire by heart")


class student:
    def __init__(self, name, rollnumber):
        self.name = name
        self.rollnumber = rollnumber

try:
    b =  student(str(input()),int(input()))
    print(b.name, b.rollnumber)
except:
    print("You messed up with your data")

        