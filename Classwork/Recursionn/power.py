#using recursion
def power(base,exp):
    if exp==1:
        return base
    elif exp!=1:
        return base*power(base,exp-1)#recursively call itself reducing exp by 1
    #if base is 2 and exp is 3If you enter base = 2 and exp = 3, the function does this:
    # power(2,3) → Since exp ≠ 1, calls 2 * power(2,2)
    # power(2,2) → Again, calls 2 * power(2,1)
    # power(2,1) → exp == 1, so returns 2
    # Backtracking: power(2,2) → 2 * 2 = 4
    # Backtracking: power(2,3) → 2 * 4 = 8

base=int(input("Enter a base:"))
exp=int(input("Enter an exponential value:"))
print("Answer:",power(base,exp))

# -------------------------------------------------------------------------------------------------------------

#using iteration
def findPower(n,exp):
    resultPower=1
    for i in range(1,exp+1):
        resultPower= resultPower*n
    return resultPower
print(findPower(2,2))
