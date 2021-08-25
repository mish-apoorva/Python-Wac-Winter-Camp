# INTERODUCTION

# COMMENTS IN PYTHON

# single line comments are           use # for single line

'''
    this                               (use single quotes 3times for multi line)
    is multi line 
    comment
'''
#------------------------------------------------------------------------------------------------------------------

# FIRST CODE 
print("Hello World!")

#----------------------------------------------------------------------------------------------------------------

print("hello", end=" ")             # to print in a single line
print("everyone!!")

print("hello", end= ' ----> ')      # to print someting in b/w the text
print("everyone!!")

print("hello",end="\n")                # to print in next line
print("everyone!!")

#---------------------------------------------------------------------------------------------------------------

print('today', 'is', 'the', 'first', 'class')      #pass many string in a single line seperated with space.
#to change the functionality of default space or wants to seperated with other symbol like(-,.,',',\n,etc)use sep=''
print('today', 'is', 'the', 'first', 'class', sep='/')
print("hello", "everyone", sep ='\n')    #seperated with new line

#-----------------------------------------------------------------------------------------------------------------------------------------

#STRINGS

#Taking input from user 
n = input("Enter your name :")
print("your name is",n)

#--------------------------------------------------------------------------------------------------------------


#VARIABLES AND DATA TYPES
'''
VARIABLES
* variables are containers for storing data values or used to give names to certain things
*value may vary
*not having specfic keyword like (for,while,etc)
*variables are case sensitive(a,A are two diff. name) and never start with numbers eg. 123a
'''
#MULTI WORDS VARIABLE NAMES

#CAMEL CASE :- each word, except the first, starts with a capital letter:
myVariableName = "Python"
#PASCAL CASE :- each word starts with a capital letter
MyVariableName = "Python"
#SNAKE CASE :- each word seperated by an underscore character.
my_variable_name = "Python"

'''
built in DATA TYPES
*Text Type       :	str
*Numeric Types   :	int, float, complex
*Sequence Types  :	list, tuple, range
*Mapping Type    :	dict
*Set Types       :	set, frozenset
*Boolean Type    :	bool
*Binary Types    :	bytes, bytearray, memoryview
'''
a = "today is a sunny day."     #string
print(a)
print(type(a))        #to check the type of a variable

b = 15      #int
print(b)
print(type(b))      

c =10.2        #float
print(c)
print(type(c)) 

d = 3+5j        #complex
e = 5j                  # j as the imaginary part
print(d) 
print(type(d))
print(e)
print(type(e))

f = True     #bool
print(f)
print(type(f))

#----------------------------------------------------------------------------------------------------------------

#TYPE CASTING
'''
    explicit type castings                  |        implicit type castings
*user defined conversion                    |    * performed without programmer intervention         
*forces an exp. to be of specific type.     |    * automatically performed by the compiler when differing data types are intermixed in an expression.  
'''

n = input()         # by default it reads input as a string
print(n)
print(type(n))

# string to int
s = str(input())               # Explicit conversion
n=int(s)                    #conversion to int
print(n)
print(type(n))

# string to float
string = str(input())
print(string)
print(type(string))
float = float(string)       #converting to float
print(float)
print(type(float))

# float to int
f= float(input())
n = int(f)                 #converting to int
print(n)
print(type(n))

# int to float
n = int(input())
f = float(n)                 #converting to float
print(f)
print(type(f))

# int to complex
n = complex(input())
c = complex(n)          #converting to complex
print(c)
print(type(c))

#----------------------------------------------------------------------------------------------------------------------------
