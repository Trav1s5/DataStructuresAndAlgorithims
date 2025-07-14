#do a factorial of any number

def factorial(n):
    #base case
    if n==0:
        return 1
    #recursive case
    else:
        return n * factorial(n-1)

print(factorial(3)) #3*2*1=6

#------------------------------------------------------------------------
from math import factorial

#using iteration
n=int(input("Enter a number:"))
factorial=1
if n>=1:
    for i in range(1,n+1):
        factorial=factorial*i
print("Factorial number is:",factorial)