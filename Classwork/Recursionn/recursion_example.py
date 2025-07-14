
# def fib(n):
#     if n==1:
#         return 1
#     if n ==2:
#         return 1
#     elif n>2:
#         return fib(n-1) + fib(n-2)
#
# for number in range(1,5):
#     print(f"{number}: {fib(number)}")



#memoisation
#f_cache={}#dictanary holds a key and a value
# value = 0
#
# def fib2(number):
#
#     if number in f_cache:
#         return f_cache[number] #to check if you have computed the base cases fib(1)
#
#     if number==1:
#         value= 1
#     elif number==2:
#        value= 1
#     elif number>2:
#         value = fib2(number-1) + fib2(number-2)
#
#     f_cache[number] = value
#     return value

# for number in range(1,100):
#     #print(number,"i",fib2(number))
#     print(f"{number}:{fib2(number)}")


#memorization cat
from functools import lru_cache
#list recently used cache

@lru_cache(maxsize=100)
def fib3(j):
    if j ==1:
        return 1
    if j==2:
        return 1
    elif j>2:
        return fib3(j-1) + fib3(j-2)

for i in range(1,999):
    print(f"(i):{fib3(i)}")


