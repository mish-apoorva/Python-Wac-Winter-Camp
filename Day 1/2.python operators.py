# PYTHON OPERATORS
'''
1. Arithmetic operators        
2. Relational operators
3. Logical operators
4. Bitwise operators
5. Assignment operators
6. Identity operators
7. Membership operators
'''
# 1.ARITHMETIC OPERATORS:- used to perform mathematical operations like addition, subtraction, multiplication and division.
'''
+    Addition	          x + y	
-	Subtraction           x - y	
*	Multiplication	      x * y	
/	Division	          x / y	
%	Modulus	              x % y	-----> gives remainder
**	Exponentiation  	  x ** y	
//	Floor division        x//y
'''
a = 20
b = 3
print("sum is :",a+b)
print("difference is :",a-b)
print("multiplication is :",a*b)
print("division is :",a/b)
print("remainder is :",a%b)
print("floor division is :",a//b)
print("pow is :",a**b) #2^3

print("sqrt 25 is :",25**0.5)

s = "Today"
print(s+s)              # + concatenate
print(5*(s + " "))      # string manipulation

# 2.RELATIONAL OPERATORS:- compares the values. It either returns True or False according to the condition
'''
<	Less than:                  	x < y
==	Equal to:                   	x == y
!=	Not equal to:                   x!= y
>=	Greater than or equal to:	    x >= y
<=	Less than or equal to:  	    x <= y
'''

x = 5
y = 3

print(x == y)
print(x < y)
print(x != y)
print(x >= y)
print(x <= y)

# 3.LOGICAL OPERATORS:- Logical operators are used to combine conditional statements.
'''
and    logical AND:both operand are True              x and y 
or     logically OR:either of the operand is True     x or y
not    logically NOT: True if operand is False        not x 
'''
a = True
b = False

print(a and b)
print(a or b)
print(not a)

# 0 for False and 1 for True
print(0 and 1)      
print(0 or 1)
print(not 1)

# 4.BITWISE OPERATORS:- Bitwise operators acts on bits and performs bit by bit operation.
'''
&	Bitwise AND 	        x & y       # The output is 1 if the corresponding bits of two operands is 1.
                                          If either bit of an operand is 0, the result of corresponding bit is 0.
|	Bitwise OR	            x | y       # The output is 1 if at least one corresponding bit of two operands is 1
~	Bitwise NOT	            ~x          #   -(a+1)   it is an uninary op. changes from 1 to 0 or 0 to 1
^	Bitwise XOR     	    x ^ y       # The result is 1 if the corresponding bits of two operands are opposite.
>>	Bitwise right shift 	x>>         # it shifts all bits towards right by certain number of specified bits by default it will take 1bit shift
<<	Bitwise left shift	    x<<         # Left shift operator shifts all bits towards left by a certain number of specified bits.
                                            The bit positions that have been vacated by the left shift operator are filled with 0. 
'''
# a = 10                # 1010
# b = 4                 #0101

# print(a & b)
# print(a | b)
# print( ~a )                 # -(10+1)
# print(a ^ b)
# print(a >> 2)               # LSB repeat two times
# print(a << 2)               # add two zeros after LSB eg 10- 1010 ---->101000 i.e 40

# 5.ASSIGNMENT OPERATORS:- used to assign values to the variables.
'''
=        is Eqaul                x = y + z 
+=       ADD AND                 a += b               # a=a+b    
-=       SUBTRACT AND            a -= b               # a=a-b 
*=       MULTIPLY AND            a *= b               #  a=a*b
/=       DIVIDE AND              a /= b               # a=a/b
%=       MODULUS AND             a %= b               # a=a%b
//=      FLOOR AND               a //= b              # a=a//b
**=      EXPONENT AND            a **= b              # a=a**b
&=       BITWISE AND             a &= b               # a=a&b
|=       BITWISE OR              a |= b               # a=a|b
^=       BITWISE XOR             a ^= b               # a=a^b
>>=      BITWISE RIGHT SHIFT     a >>= b              # a=a>>b
<<=      BITWISE LEFT SHIFT      a <<= b              # a=a<<b>> 

'''
a= 5
b= 4

a = 5
print(a)

a += b
print(a)

a -= b
print(a)

a *= b
print(a)

a /= b
print(a)

a %= b
print(a)

a **= b
print (a)

#IDENTITY OPERATORS:- used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
'''
is              a is b
is not          a is not b
'''
a = [1,2,3]
b = [1,2,3]
c = a

print(a is b)       # returns False bcoz a is not the same object as b, even if they have the same content.
print(a is c)       # returns True bcoz c is the same object as a

print(a is not b)
print(a is not c)

# MEMBERSHIP OPERATOR:- used to test if a sequence is presented in an object.
'''
in              a in b
not in          a not in b
'''
a = ['apple', 'mango', 'grapes', 'banana']

print('mango' in a)
print('orange' not in a)

#----------------------------------------------------------------------------------------------------------------
'''
Operator        	Description	                                            Associativity
( )             	Parentheses                                         	left-to-right
**                 	Exponent 	                                            right-to-left
*  /  %         	Multiplication/division/modulus                     	left-to-right
+  -	            Addition/subtraction	                                left-to-right
<<  >>          	Bitwise shift left, Bitwise shift right	                left-to-right
<  <=               Relational less than/less than or equal to                  ''
>  >=	            Relational greater than/greater  than or equal to	    left-to-right
==  !=	            Relational is equal to/is not equal to              	left-to-right
'''