# print numbers from 10 downwards

def countdown(n):

    #base case when to stop
    if n<0:
        print("done!")
    #Recursive call-call the function again
    else:
        print(n)
        countdown(n-1) #call itself with n-1

countdown(10) #countdowns from 10 to 0