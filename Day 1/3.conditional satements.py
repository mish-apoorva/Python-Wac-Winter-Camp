#CONDITIONAL STATEMENT
'''
if condition
elif condition          "if the previous conditions were not true, then try this condition"
else condition          " if 'if' or 'elif' condition is  not true, then try this condition"
Nested if               "we have if statements inside if statements, this is called nested if statements."
'''
# SYNTAX
'''
if condition :                                  
    statements
elif condition :
    statements
else condition :
    statements
satements
'''

# IF CONDITION

a = 10
b = 20

if b > a:
  print("b is greater than a")
print("the given condition is true")        # if the given cond. is false then it print only this statement


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ELIF CONDITION

a = 10                          # a= int(input("enter the value of a"))
b = 10
if b > a:
  print("b is greater than a")          #in case if cond. is false then it will go for elif condition
elif a == b:
  print("a and b are equal")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#ELSE CONDITION

a = 50
b = 20
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")          # else cond. will execute only when if and elif cond. are NOT TRUE.

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# NESTED IF

x = 40

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1.TO CHECK WHETHER THE GIVEN NUMBDR IS EVEN OR ODD

n = int(input("Enter a number :"))

if n%2 == 0:
    print("Even")
else:
    print("Odd")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2.TAKE THE INPUT FROM THE USER AND DIVIDED IT BY 3 AND THE PRINT THE REMAINDER 

#NOTE:- WHEN WE DIVIDE A NUMBER WITH ANY NUMBER THE REMAINDER WILL ALWAYS BE IN RANGE[0, b-1]  eg. a%b = [0, b-1]

n= int(input("Enter a Number :"))
if n%3 == 0:
    print("zero")
elif n%3 == 1:
    print("one")
else:
    print("two")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3.FIZZ BUZZ (multiple of 3 --> Fizz, multiple of 5 --> Buzz, both the --> FizzBuzz)

n= int(input("Enter a Number :"))

if n%3 == 0 and n%5 == 0 :
    print("FizzBuzz")
elif n%3 == 0 :
    print("Fizz")
elif n%5 == 0 :
    print("Buzz")
else :
    print(n)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 4.Design Calculator

m = int(input("Enter first Number :"))
n = int(input("Enter second Number :"))

op = input("Enter Operator :")

if op == "+" :
    print(m+n)
elif op == "-" :
    print(m-n)
elif op == "*" :
    print(m*n)
elif op == "/" :
    print(m/n)
elif op == "**" :
    print(m**n)
else :
    print("Wrong operator")
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 5.Leap Year

# year is divisible by 400 ---> leap Year
# year divisible by 100 and not by 4 ---> not a leap year
# year divisible by 4 ---> leap Year
# else not a leap year

n = int(input("enter a year :"))

if n % 400 == 0:
    print('Leap Year')
else :
    if n % 100 == 0:
        print("Not a Leap Year")
    elif n % 4 == 0:
        print('Leap Year')
    else:
        print("Not a Leap Year")
