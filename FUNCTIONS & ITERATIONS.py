#Give repetetive lines of code a name & use it where ever needed by calling the function. D-R-Y = Don't repeat yourself.
#In python we start a fn with def keyword = def()



def simplefn():  #function start by definining a function simplefn()
    print("These lines of code are in the function")
    print("This is a function") #function end
print("Now we are going to call a function & print")
simplefn() #calling function




#----------------------FINDING THE LARGEST  & smallest ---------------

lrgstr = max('Hafeezuddin')     #max predefined function #'Hafeezuddin' is the argumment
print(lrgstr)

smlnum = min(14, 25 , 300)      #min predefined function
print(smlnum)


#---------------------------- An another example of function------------
x=5
def lyrics_song():
    print("oh lalalalala lalalala")
    print("uhlalalallalale oooo uh lalallaeo")

print(type(x))
lyrics_song()
x=x+2
print(x)

#NOTE: DEF STATEMENT DOESNOT AUTOMATICALLY RUN THE CODE. 
#You must invoke the function in order to execute the statements inside the function.

#---------- parsing the values as argument & evaluating--------------

def eval(x):
    if x==10:
        print("The value is 10")
    elif x==20:
        print("The value is 20")
    else:
        print("No valid input given")

eval(20) 
eval(10)
eval(25)

#---------------------------------example 2 of parsing string as argument and eval---------------------------------------
def eval(lang):
    if lang=="rn":
        print("Roman")
    elif lang=="eng":
        print("English")
    else:
        print("No valid input given")
eval("eng")
eval("rn")


#----------------usage of return keyword within the program-----------
def greet():
    return "Hello"
print("smith", greet())
print("Jones", greet())

#-----------------Another example-------------
def evall(lang):
    if lang=="en":
        return "HELLO"
    elif lang=="rn":
        return "Hola"
print(evall("rn"), "Smith")

#--------DEFINING MORE THAN ONE PARAMETER----------

def sam(a,b):    #PARSING MULTIPLE PARAMETERS IN A FUNCTION
    c=a+b
    return c
x=sam(2,3)
print(x)


#----------------------MISCLEANEOUS---------------------------
x = 'banana'
y = max(x)
print(y)


def func(x) :
    print(x)
func(10)
func(20)




def stuff():
    print('Hello')
    return
    print('World')
stuff()




def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('fr'),'Michael')




def computepay(h,r):
    if h > 40:
        p = 1.5 * r * (h - 40) + (40 *r)
    else:
        p = h * r
    return p
    
hrs = input("Enter Hours:")
hr = float(hrs)
rphrs = input("Enter rate per hour:")
rphr = float(rphrs)

p = computepay(hr,rphr)
print("Pay",p)



zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)


smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)

if smallest is None :
     smallest = value