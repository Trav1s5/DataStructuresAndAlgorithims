#;This method is via using classes using LIST!!
class simpleStack:
    def __init__(self):
        #initialized an empty list that will hold stack elements
        self.items=[]

    #for an empty list
    def is_empty(self):
        # returns true if stack is empty otherwise returns false
        return len(self.items)==0

    #adding elements to the top of the elements
    def push(self,item):
        self.items.append(item)

    #to remove elements from the top of the stack
    def pop(self):
        if self.is_empty():
            raise Exception("List is empty")
        else:
            return self.items.pop()

    #to peek elements at the top
    def peek(self):
        if self.is_empty():
            raise Exception("Empty stack!!")
        else:
            return self.items[-1]

    #return the number of all the items in the stack
    def size(self):
        return len(self.items)

    #for printing
    def print_stack(self):
        print("Stack from top to bottom",self.items)
        return

if __name__ == "__main__":
    #instatiate the class for simpleStack by creating an object for it
    stack1=simpleStack()

    #push some elements:
    stack1.push(100)
    stack1.push(200)
    stack1.push(300)

    stack1.print_stack()

    #to peek the top element
    print("What is the top element:",stack1.peek())

    #check if stack is empty
    print("is stack is empty:",stack1.is_empty())

    # remove elements
    stack1.pop()
    stack1.print_stack()

    #peek top
    print("The new top element is:",stack1.peek())

    #to pop all the elements
    stack1.pop()
    stack1.pop()
    print("is the stack empty:",stack1.is_empty())

#the following is using linked list via stack>>>>>>>>>>>>>>