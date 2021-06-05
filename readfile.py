f=open("a.txt",'r')
print(f.read()) #PRINTS ENTIRE CONTENT OF THE FILE
f.close()

f=open("a.txt",'r')
print(f.readable()) #Gives TRUE BOOLEAN VALUE IF FILE IS READABLE ELSE FALSE 
print(f.readline()) #PRINTS TOP LINE
f.close()

f=open("a.txt",'r')
print(f.readlines()) #puts sentences in an array
print(f)

f=open("a.txt",'r')
for i in f:
    print("Hello")
print(f.readlines()) #puts sentences in an array
    
f=open("a.txt",'rt')
print(f.read())

f=open("a.txt",'rb')
print(f.read())