# NESTEDC LOOPS
for i in range(5):
    for j in range(5):
        print(i, end = ' ')
    print()

# STAR PATTERN
n = int(input())
for i in range(n):
    for j in range(n):
        print(" *", end =' ')
    print()

# using string manipulation
n = int(input())

for i in range(n) :
    print('*'*n)

# print pattern of right anghle triangle

n = int(input())
for i in range(n):
    for j in range(i+1):
        print(' *', end =' ')
    print()

# using string manipulation
for i in range(n):
    print(' * '*(i+1))

#---------------------------------------------------------------------------------------------

'''
Break and Continue statement
'''
# Break statement:- With the break statement we can stop the loop even if the condition is true:

for i in range(10):
    if i == 7:
        break   #loop exixting statement
    print(i)

# Continue statement:- With the continue statement we can stop the current iteration, and continue with the next:

for  i in range(10):
    if i%2 == 0:
        continue # loop skiping statement
    print(i)

#--------------------------------------------------------------------------------------------------------------------------

# To Check Whether it is Prime or Not
n = int(input())

is_prime = True

#temp = int(n**0.5)
for i in range(2, n):   #[2,n-1], [2,n//2 +1 ],[2,sqrt(n)+1]
    if n%i == 0:
        is_prime = False
        break
if is_prime:
    print('It Is a Prime Nummber')
else:
    print('Not a Prime Nummber ')

#nCr
# n!/r!(n-r)!

n = int(input())
r = int(input())
nr = n-r

fact_n, fact_r,fact_nr = 1, 1, 1, 
for i in range(1, n+1):
    fact_n *= i

for i in range(1, r+1):
    fact_r *= i

for i in range(1, nr+1):
    fact_nr *= i

ans = fact_n/(fact_r*fact_nr)
print(ans)
