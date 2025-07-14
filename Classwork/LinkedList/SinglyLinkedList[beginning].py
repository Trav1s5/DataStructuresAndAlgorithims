#OOP IMPLEMENTATION OF THE FIRST SINGLYLINKEDLIST
#AT THE BEGINNING
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None #linkedlist has nothing yet
    def insertAtTheBeginning(self, newData):
        new_node = Node(newData) #immediaetly creates a node
        new_node.next=self.head  #.next will point its node to the beginning of the list

        self.head=new_node       #head will be the new data

    def printLinkedList(self):
        temp=self.head
        while temp:
            print(temp.data , end=' ')
            temp=temp.next
        print()

if __name__=='__main__':
    llist=LinkedList() #call the method for printing
    llist.insertAtTheBeginning("Fox")
    llist.insertAtTheBeginning("Brown")
    llist.insertAtTheBeginning("Quick")
    llist.insertAtTheBeginning("The")


    llist.printLinkedList()