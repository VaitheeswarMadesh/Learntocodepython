#Learn Python programming using Notebook authered by Hafeezuddin Shaik
#EASY TO CODE/ IF YOU ARE NEW TO PROGRAMMING PYTHON IS BEST LANGUAGE TO START.
#Current version while creating this notebook is Python 3.7.X

# ------- VARIABLES PRINTING & DATA TYPES--------

#Simple Print Statement
print("Hello World!")   

print("123456")     #Anything written in " " & ' ' is treated as string

a="1233456"
print(type(a))     #Prints the data type of variable a. Variable holds the value assigned to it in a memory unit.
print(a)

b=1010             #b is a variable & is assigned a number
print(type(b))
print(b)

c=4+3j             # Variable c is assigned a complex number
print(type(c))
print(c)

d=4.2              # Variable d is assigned with a floting number
print(type(d))
print(d)

#NOTE: Python is case sensitive Language. Variable K is different from k.

k=145
K=12.3

print(k)
print(type(k))

print(K)
print(type(K))

#--------------------------TYPE COVERSIONS----------------------------------------------------------------

z=19.5
print(type(z))
print(int(z))


q="19"
r=2
z=int(q)*int(r)     #string to int conversion
print(z)

q="19.5"
r=2
z=float(q)*int(r)    #string to float conversion
print(z)


#------------------------------------------------EXPRESSIONS------------------------------------------
