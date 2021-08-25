#LIST
mylist = ["c", "c++", "python", "java", "kotlin"]               #used to store multiple items in a single variable.
print(mylist)
print(len(mylist))              # to print length of the list             
print(mylist[1])                # to access a specfic item fromm list
print(mylist[2:5])          # return item of list from index 2 to index 5 but exclude the item at index 5
print(mylist[-4:-1])

# # RANGE FUNCTION
# #range(start=, stop, step=)
print(list(range(10)))
print(list(range(0, 10, 2)))

        



# LOOPS
'''
WHILE LOOP              we can execute a set of statements as long as a condition is true.
FOR LOOP                used for iterating over a sequence 
'''
# WHILE LOOP
i = 0   #counter
while i< 10 :   #condition
    print('Hello')
    # i = i + 1  #step size-increment value
    i += 1


#SUM OF N NATURAL NUMBERS USING WHILE LOOPS
n = int(input("Enter Number: "))

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

print("The sum is", sum)

# FOR LOOP
for i in range(10):
    print(i)
for i in range(1, 10, 2):
    print(i)

# TABLE
n= int(input("Enter a Number :"))

for i in range(1, 11):
    print(n*i)

# ODD NUMBERS IN RANGE 1- 20
for i in range(1, 20, 2):
    print(i)

# ODD NUMBERS IN REVERSE
for i in range(19, 0, -2):
    print(i)

# SUM OF N NATURAL NUMBERS:
num = int(input("Enter a Number :"))
sum = 0
for i in range(1, num+1):
    sum += i

print("Sum is :", sum)


# FACTORIAL OF A NUMBER:

n = int(input("Enter a Number :"))
fact = 1
for i in range(1, n+1):
    fact= fact*i

print("Factorial is:", fact)

