class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None #linkedlist has nothing yet

    def insertAtTheBeginning(self, newData):
        new_node = Node(newData)  # immediaetly creates a node
        new_node.next = self.head  # .next will point its node to the beginning of the list

        self.head = new_node  # head will be the new data

    def insertAtTheEnd(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last = self.head
        while last.next:
            last=last.next#holds till where the last node points to none
        last.next=new_node

    def printLinkedList(self):
        temp=self.head
        while temp:
            print(temp.data , end=' ')
            temp=temp.next
        print()

if __name__=='__main__':
    llist=LinkedList()
    llist.insertAtTheBeginning("Fox")
    llist.insertAtTheBeginning("Brown")
    llist.insertAtTheBeginning("Quick")
    llist.insertAtTheBeginning("The")


    llist.printLinkedList()
    llist.insertAtTheEnd("jumps")
    llist.insertAtTheEnd("over")
    llist.insertAtTheEnd("the")
    llist.insertAtTheEnd("fence")

    llist.printLinkedList()