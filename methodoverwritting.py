class Person:		
    def __init__(self, name, idnumber):     #method 1 for initialization __init__ is must
     self.n=name
     self.s=idnumber
    
    def guddu(self):
     print("hi,i'm guddu")
    
class Student(Person):
    def __init__(self, name, idnumber,salary):  #child class
     super().__init__(name, idnumber)
     self.s=salary
   
    def guddu(self):          #method over writing
     print("hello,world")

abc=Student("john",123,89076)
print(abc.n)
abc.guddu()

pqr = Person("Lorem ipsum",876)
print(pqr.n)
