# def fibonacci(n):
#     if n == 1:   # we return first term
#         return 1
#     elif n == 2:  # we return the second term
#         return 1
#     elif n > 2:  # we return sum of the previous two terms
#         return fibonacci(n-1) + fibonacci(n-2)
# for n in range(1, 4):
#     print(f"{n} : {fibonacci(n)}" )



# for n in range(1, 101):
#     print(f"{n} : {fibonacci(n)}" )

# MEMOIZATION:
# LONG
# The cure to this is memoization
# Store the values for recent function calls
# so future calls do not have to repeat the already computed calls
# Cache values

fibonacci_cache = {}

def fibonacci_2(number):
    # A bit of type validation
    if type(number) != int:
        raise TypeError("n must be a positive int")

    if number < 1:
        raise ValueError("n must be a positive int")

#     """We compute """
#     # if we have cached the value then return it
    if number in fibonacci_cache:
        return fibonacci_cache[number]
#
#     # compute the nth term
    if number == 1:
        value = 1
    elif number == 2:
        value = 1
    elif number > 2:
        value = fibonacci_2(number - 1) + fibonacci_2(number - 2)

    # Then store the computed value in our cached dictionary then return it
    fibonacci_cache[number] = value
    return value

for n in range(1, 1):
    print(n, ":", fibonacci_2(n))

# Another way to do this is to use a decoration function
# lru_cache
# L - Least. R  -> Recently. U -> Used C -> Cache
# IT PROVIDES A ONE LINE WAY TO ADD MEMOIZATION
from functools import lru_cache

@lru_cache(maxsize=1000)
def fib(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fib(n - 1) + fib(n - 2)

for n in range(1, 2099):
    print(n, ":", fib(n))
#
# # Golden Ratio
for n in range(1 ,51):
    print(fib(n+1) / fib(n))