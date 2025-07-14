#recursion
def fib(n):
    if n==0 :
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print("fib 3 is",fib(3))
#to generate fibonacci series

for i in range(7):
    print(fib(i))
#------------------------------------------------------------

#iteration
n=int(input("How many terms the user wants to print?"))
n1=0
n2=1
count = 0
if n<=0:
    print("Please enter a positive integer!")
elif n==1:
    print("The fib sequence is upto:")
    print(n1)
else:
    print("the fib sequence is:")

    while count <n:#loop runs as long as count is < than n
        print(n1)
        nth=n1+n2 #stores next term by adding previous terms
        n1=n2 #n1 moves to n2
        n2=nth #while n2 becomes next number in sequence
        count+=1# increment to ensure count reaches n


