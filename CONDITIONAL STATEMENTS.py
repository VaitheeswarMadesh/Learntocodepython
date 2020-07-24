#conditional statement brings intelligence to any programming language
#Eg: if this condition is true ---- DO THIS ----- ELSE DO THIS

#------------------IF CONDITIONAL STATEMENT---------
#---------------------INSTANCE I--------------------

x=1000
if x>100:
    print("Value of x is greater than 100")
else:
    print("value of x is less than 100")

#---------------------INSTANCE II-------------
#Whatever you enter as input, input function convert it into a string.
# if you enter an integer value still input() function convert it into a string. You need to explicitly 
# convert it into an integer in your code using typecasting.


p = input("ENTER THE VALUE OF P:")
p=int(p)     #TYPE CONVERSION FROM STRING TO INTEGER
if p<=10:
    print("Hyderbad is a Great City")
if p>=10 and p<=20:
    print("Hyderabad is a Metropolitan city")
else:
    print("Hyderabad is in Telangana")

#----------------------------------------------------------------------------------------------------------------
# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number. 

hrs = input("Enter Hours:")
h = float(hrs)

rate=input("RATE")
r=float(rate)

if h<=40:
    pay=h*r
    print(pay)

if h>=40:
   pay=(40*r)+((h-40)*1.5*r)
   print(pay)
    
#-------------------------------------------ELIF----------------------------------------------------------------------
score = input("Enter Score: ")
sr=float(score)
if sr>1.0:
    print("OUT OF RANGE")
elif sr>=0.9:
	print("A")
elif sr>=0.8:
	print("B")
elif sr>=0.7:
	print("C")
elif sr>=0.6:
	print("D")
elif sr<0.6:
	print("F")

#-------------------------------------------------try catch statement---------------------------------------------------
#used to handle errors and prevent from causing interuptions in program flow.
n="aster"
try:
    n=int(n)
except:
    n=-1
print("HELLO", n)

#----------------------------------------------------ODD & EVEN-----------------------------------------------------------

k=input("Enter the Value:")
k=float(k)
if k%2==0:
    print("The Number is Even")
else:
    print("The number is ODD")

#---------------------------------------------------------------------------------------------------------------------------

