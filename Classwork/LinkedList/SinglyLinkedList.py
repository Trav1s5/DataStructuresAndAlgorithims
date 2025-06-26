# CREATION OF SINGLY  LINKED LIST

class SinglyLinkedList:
    def __init__ (self,value,newNode =None):
        self.value=value
        self.nextNode=newNode

snode1= SinglyLinkedList("1")
snode2= SinglyLinkedList("2")
snode3= SinglyLinkedList("3")
snode4= SinglyLinkedList("4")

#linking the snodeN to each other
snode1.nextNode=snode2
snode2.nextNode=snode3
snode3.nextNode=snode4

#printing
currentNode=snode1
while True:
    #checks a condition that is always true
    print(currentNode.value,">>>", end =' ')#current Node> head

    if currentNode.nextNode is None:
        print("None")
        break
    currentNode=currentNode.nextNode

