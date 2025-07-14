"""1]Define a recursive function that takes two integers as input and returns their product using
repeated addition, without employing the multiplication operator. """
def productUsingRepeatedAddition(a,b):
    #base case
    if b==0:
        return 0
    #recursive case
    elif b>0:
        return a+ productUsingRepeatedAddition(a,b -1)
    else:
         return -productUsingRepeatedAddition(a,-b)#if b is negative it converts it to positive and flips the sign of the result
print(productUsingRepeatedAddition(2,2))

"""2]Define a recursive function that computes the result of raising a given base to a specified 
exponent, without using the exponentiation operator(**) """

def raisingBaseWithoutExp(b,exp):
    #base case
    if exp==0:
        return 1
    #handle negative exp
    elif exp<0:
        return 1 / raisingBaseWithoutExp(b,-exp)
    else:
        return b *raisingBaseWithoutExp(b,exp-1)
print(raisingBaseWithoutExp(1,23))


"""3]Implement a recursive function that prints all integers from a given number n down to 0"""

def countdown(n):
    #base case
    if n<0:
        print(" ")
    #recursive case
    else:
        print(n)
        countdown(n-1)

countdown(10)

"""4]Implement a recursive function that prints all integers from 0 up to a given number n by modifying 
the previous countdown function. """

def countup(n):
    #base case
    if n<0:
       return None
    #recursive case
    else:
        countup(n-1)
        print(n)

countup(5)

"""5]Write a recursive function that takes a string as input and returns a reversed copy of the string, 
using only string concatenation."""

def reverseString(str):
    #base case
    if len(str)==0:
        return ""
    elif len(str)==1:
        return str
    else:
        return str[-1]+reverseString(str[:-1])
print(reverseString("Travis"))

"""6]Write a recursive function that determines whether a given integer n is a prime number by 
checking for divisibility by integers less than n"""

def primenumber(n,divisor=None):
    """recursively checks if the n is prime :boolean returns true if n is prime and false if not"""
    #base case
    if n<=1: # less than one not prime
        return False
    if n<=3:
        return True #2 and 3
    if n% 2==0:
        return False #means  if n is divisible by 2

    #initializing the divisor
    if divisor is None:
        divisor =3
    if divisor* divisor>n:
        return  True
    if n % divisor==0:
        return False

    #recursive case
    return primenumber(n,divisor+2)

print(primenumber(2))



"""7]Write a recursive function that takes in one argument n and computes Fn, the nth value of the 
Fibonacci sequence. Recall that the Fibonacci sequence is defined by the relation Fn = Fn−1 + Fn−2 
where F0 = 0 and F1 =1 """

def fibonacci(n):
    #base cases
    if n<=0:
        return 0 #f0=0
    if n==1:
        return 1#f1=1
    #recursive call
    else:
        return fibonacci(n-1)+fibonacci(n-2)#fib formulae
print(fibonacci(8))

