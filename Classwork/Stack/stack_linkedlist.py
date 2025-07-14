# Sometimes stacks are implemented using linked list
#to avoid resizing issues  with lists and to practice pointer manipulation

class StackNode:
    def __init__(self,value):
        self.value=value #to store the node's data
        self.next=None#points to the next node(below in the stack)

#stack implementation with LinkedList
class LinkedListStack:
    def __init__(self):
        self.top=None

    #for an empty stack
    def is_empty(self):
        return self.top is None

    #to push a node
    def push(self,value):
        #creates a new Node with the value
        newNode=StackNode(value)
        #the new node's next pointer points to the current top node
        newNode.next=self.top
        #update the top pointer to the new node(new top of the stack)
        self.top=newNode

    #to po a node
    def pop(self):
        if self.is_empty():
            raise Exception("Cannot pop from empty stack!")
        #if stack is empty raise error

        #retrieve value from top node
        popped_value= self.top.value

        #move top pointer to next node down the stack
        self.top=self.top.next

        #return popped value
        return popped_value

    #to peek
    def peek(self):
        #return top element without removing it
        if self.is_empty():
            return Exception("Cannot peek to an empty stack")
        return self.top.value

    def display(self):
        #print stack from top to bottom
        current = self.top
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        print("Stack from top to bottom:", "->".join(values))

#example usages:
if __name__=="__main__":
    stack_1=LinkedListStack()
    stack_1.push(100)
    stack_1.push(200)
    stack_1.push(300)

    stack_1.display() #outputs:300->200->100

    print("Peek top:",stack_1.peek())#returns 300

    print(stack_1.pop())#outputs 300 and removes it from the stack
    stack_1.display() #outputs 200->100









