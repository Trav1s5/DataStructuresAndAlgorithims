# A stack is a data structure that follows the LIFO principles.
#Think of it in this way : you have a stack of plates and you want to put them in a box so you add them from the  top (push) and you take plates from the top (pop)
#You can only access the top ones not the bottom ones

"""
Basic stack operations include:

push:Adds an element to the top of the stack
pop:removes the top element of the stack
Peek/Top:Looks at the top element of the stack
IsEmpty:Checks if the stack has any element if it has it returns false if it does not have it  returns true

"""

#we will use the first python inbuilt method for stacks:list
#coz it supports .append() push() and pop() methods

# USING  A LIST!!!
stack=[] #creates an empty list to represent the stack
stack.append(100) #adding an element to the top of the stack
stack.append(200)
stack.append(300)
stack.append(400)
stack.append(500)
stack.append(600)
print("Stack has the following:",stack) #prints the result


#if you want to peek/use Top we do the following(last element of the list)
top_element = stack[-1] #access the last element without removing it (-1 coz it will access the last element)
print("the top element is:",top_element)

#to check if it is empty
if len(stack)==0:
    print("List is empty")
else:
    print("List is not empty")

#Next is using custom classes in implementing stacks>>>>>>>>>