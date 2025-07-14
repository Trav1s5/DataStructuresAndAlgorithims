class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None  # linkedlist has nothing yet

    def insertAtTheBeginning(self, newData):
        new_node = Node(newData)  # immediaetly creates a node
        new_node.next = self.head  # .next will point its node to the beginning of the list

        self.head = new_node  # head will be the new data

    def insertAtTheEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next  # holds till where the last node points to none
        last.next = new_node

        # DELETION
        #:FROM BEGINNING

    def deleteFromBeginning(self):
        if self.head is None:
            return "LinkedList is empty"
        self.head = self.head.next  # assigned self.head,next which is holding "quick" thus the new head becomes quick

        # FROM END

    def deleteFromEnd(self):
        if self.head is None:  # empty
            return "LinkedList is Empty"

        if self.head.next is None:  # only one node
            self.head = None
            return
        temp = self.head  # assigned to first Node

        while temp.next.next:  # 2nd  node from current node
            temp = temp.next
        temp.next = None

    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()


if __name__ == '__main__':
    # beginning
    llist = LinkedList()
    llist.insertAtTheBeginning("Fox")
    llist.insertAtTheBeginning("Brown")
    llist.insertAtTheBeginning("Quick")
    llist.insertAtTheBeginning("The")

    # end
    llist.printLinkedList()
    llist.insertAtTheEnd("jumps")
    llist.insertAtTheEnd("over")
    llist.insertAtTheEnd("the")
    llist.insertAtTheEnd("fence")
    llist.printLinkedList()  # print

    # deleteFromBeginnig
    llist.deleteFromBeginning()
    llist.insertAtTheBeginning("A")
    llist.printLinkedList()

    # deleteFromEnd
    llist.deleteFromEnd()
    llist.insertAtTheEnd("wall")
    llist.printLinkedList()






