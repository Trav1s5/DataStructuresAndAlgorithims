# FIRST WE DEFINE A NODE CLASS TO REPRESENT EACH ELEMENTS IN THE CIRCULAR DOUBLY LINKED LIST
class CircularListNode:
    def __init__(self, value):
        # We store the actual data /value
        self.value = value

        # next-node is an attribute of type pointer that will point to the next node in the list
        # Initially when the node is created we dont know the next node so we set it to None or null
        self.next_node = None
        # having previous node usually points to the previous node in the list
        # Initially we will set it to None since the list is empty at this point
        self.previous_node = None


# THEN WE DEFINE THE CIRCULARDOUBLYLINKEDLIST CLASS TO MANAGE NODES AND OPERATIONS
class CircularDoublyLinkedList:
    def __init__(self):
        # we need to tell the compiler about the first node in the head
        # here the start_node will be our head and it will keep track of the 1st Node in the list(The head)
        # if the list is empty start_node is None
        self.start_node = None

    # THIS METHOD INSERTS A NEW NODE WITH THE GIVEN 'VALUE' AT THE END OF THE CIRCULAR DOUBLY LINKED LIST
    def insert_at_end(self, value):
        # =>1st create a new node object with the given value
        new_node = CircularListNode(value)
        # =>2nd check if our list is empty
        if self.start_node is None:
            # if the list is empty this block will be executed
            # since the list is empty this new node will be the only node in our list
            # then for a circular list this node points to itself in both directions
            new_node.next_node = new_node
            # the next node after(new_node is itself)
            new_node.previous_node = new_node
            # the previous node before (new_node is itself)

            # also we need to update the start_node pointer to this new_node
            self.start_node = new_node
        else:
            # means the list has contents
            # we need to add the new node at the end
            # last_node that currently comes before the start_node
            # Remember this is a cirularly doubly linked ;est
            # Now we have a special concept called chained attribute access or attribute chaining
            # here it is:
            # self.start_node.previous_node means:
            # 1]'self.start_node'=>give us the first node in the line
            # 2]'previous_node'=>accesses the node that comes before the start_node

            # in context
            # You are navigating object references thru chained attributes - essentially following links(pointers) btwn objects

            # in data strucutres [like linked list] this is also described as:
            # [I]Pointer tranversal in oop
            # [II]Link following in node-based structures

            # so self.start_node.previous_node is an example of pointer tranversal via attribute chaining in a linked structure
            # this works because the list is circular so th enode before the first node is the last node
            last_node = self.start_node.previous_node

            # now we link the new_node into the list
            # 1st the current last_node'next_node_' should point to the new_node
            last_node.next_node = new_node

            # 2nd the new_node's 'previous_node' should point back to the last_node
            new_node.previous_node = last_node

            # 3rd the new_node's 'next_node' should point to the start_node to maintain circularity
            new_node.next_node = self.start_node

            # lastly the start_node's 'previous_node' should now point back to the new_node, which is the new last node
            self.start_node.previous_node = new_node

    # HERE WE WILL INSERT A NEW NODE WITH THE GIVEN 'VALUE' (passed as a parameter) AT THE BEGINNING OF THE CIRCULAR DOUBLY LINKED LIST
    def insert_at_beginning(self, value):
        # To optimise our code we are going to reuse the insert_at_end method to add the node at the end first
        self.insert_at_end(value)
        # after adding the new_node at the end we move the start_node pointer backward to the new node
        # here is the mark down
        # -'self.start_node' is currently the first node
        # 'self.start_node.previous_node' is the node just added at the end
        # By setting start_node to start_node.previous_node we simply make the new node the first node
        self.start_node = self.start_node.previous_node

    # TO REMOVE THE FIRST NODE FOUND WITH THE SPECIFIED VALUES
    def remove_by_value(self, value):
        # if the list is empty , then ofcourse, there is nothing to remove
        if self.start_node is None:
            print("The list is empty.Cannot remove any node.")
            return

            # if not we start by searching from the start_node
        current_node = self.start_node

        # we will iterate through the llist until we come back to the start_node since it's circularly linked list
        while True:
            if current_node.value == value:
                # we only enter this block if we find the node to remove
                # after finding the node to remove there are a few cases we need to consider
                # the first case is that the list has only one node(which is current_node)
                if current_node.next_node == current_node:
                    # since it's the only node, removing it makes the list empty
                    self.start_node = None
                else:
                    # the second case , is that the list has multiple nodes
                    # so inorder to remove current_node we need to announce our intentions to our neighbours
                    # by updating the links of these neighbours
                    # remember the pointer traversal via attribute chaining in as that 'current_node.previous_node.next_node = current_node.next_node which basically implies
                    # The node before the current_node should nowpoint forward to the node after current_node\
                    current_node.previous_node.next_node = current_node.next_node

                    # 'current_node.next_node.previous_node = current_node.previous_node' Implies that,
                    # -the node after current_node should now point backward to the node before current_node
                    current_node.next_node.previous_node = current_node.previous_node

                    # if we are removing the strat_node , movethe start_node pointer forward
                    if current_node == self.start_node:
                        self.start_node = current_node.next_node

                        # By this point the node is removed and we can peacefully exit the method
                return

                # we now move to the next node in the list
            current_node = current_node.next_node

            # if we by any chance have mannaged looped back to the start_node, the value was not found
            if current_node == self.start_node:
                print(f"Value {value} not found in the list.")
                break

    # DISPLAYING THE VALUES OF THE NODES IN THE LIST STARTING FROM THE START_NODE AND MOVING FORWARD

    def show_list_forward(self):
        # we start by checking if the lsit is empty if so print a message and exit the method using return
        if self.start_node is None:
            print("The list is empty.")
            return

        # set a temporary attribute to aid us loop by assigningit to the start_node
        current_node = self.start_node
        # then we create an empty list to collect the string representation(convert the sata part of the node to string) of the node values
        values_list = []

        # tranverse through the list until we come back to the start_node
        while True:
            # Add the current node's value to the list as a string
            values_list.append(str(current_node.value))

            # Then we do our incrementation here by utilizing the pointers
            current_node = current_node.next_node

            # we then check a condition where we have completed a full circle , and if so we MAKE A STOP
            if current_node == self.start_node:
                break

            # we can format output but it is not a must however we shall do it therwise:
            # so this is how we do it.
            # =>we join all the values in 'values_list' into a single string separeted by '->'

            # Explanation:
            # '->' is a string separator
            # 'join(values_list)   ' takes all elements in 'values_list' and concatenates them into one string
            # putting '->' between each element
            # for example: if values_list =['5','10','15'] the result becomes '5->10->15'
        output_string = " -> ".join(values_list)
        # prints the resulting string
        print(output_string)

    # HERE WE ARE ATTEMPTING TO DISPLAY THE VALUES OF THE NODES IN THE LIST STARTING FROM THE LAST NODE AND MOVING BACKWARD
    def show_list_backward(self):
        # if its an empty list print the message and exit the method via return
        if self.start_node is None:
            print("The list is empty.")
            return

        # here the last node is the one before the start_node(since it is a circular linked list)
        last_node = self.start_node.previous_node
        # Why not store a self.last_node separetely?
        # Coz it adds redundancy and risks de-synchronize
        # instead we just access what we need through the links.

        # FOR THE PRINTING PART ; START FROM THE LAST NODE:
        current_node = last_node
        # create an empty list to collect the string representation of node values
        values_list = []

        # Traverse the list backward until we come back to thelast_node
        while True:
            # Add the current node's values to the list a string
            values_list.append(str(current_node.value))

            # move to previous node
            current_node = current_node.previous_node

            # stop if we have completed a full circle
            if current_node == last_node:
                break

        # Join all the vlaues in 'values_list' into a single string separated by '<-'
        # -'<-' is our separator that now indicates backward direction
        # - 'join(values_list)' concatenates all elements in 'value_list' with '<-' between them
        # e.g if we have values_list = ['30','20','10'] , the result will be '30 <- 20 <-10 '
        output_string = " <- ".join(values_list)

        # print the resulting string to show the list
        print(output_string)

# THE MAIN BLOCK
if __name__ == "__main__": #Create a node by instantiating that class via the creating of an object
    my_circular_list = CircularDoublyLinkedList()

    #then we insert values by calling the insertion method we created
    my_circular_list.insert_at_end("Quick")
    my_circular_list.insert_at_end("Brown")
    my_circular_list.insert_at_end("Fox")
    print("List after inserting at the end:")

    #call the print forward method
    my_circular_list.show_list_forward()

    my_circular_list.insert_at_beginning("The")
    print("List after inserting at the beginning:")
    my_circular_list.show_list_forward()

    print("List displayed backwards")
    my_circular_list.show_list_backward()

    my_circular_list.remove_by_value("quick")
    print("List after removing Quick:")
    my_circular_list.show_list_forward()

    my_circular_list.remove_by_value("Quick")#not found
    my_circular_list.remove_by_value("Slow")#not found

    my_circular_list.remove_by_value("Brown")
    print("List after removing Brown:")
    my_circular_list.show_list_forward()

    #attempting to empty the list by removing the removing elements
    my_circular_list.remove_by_value("The")
    my_circular_list.remove_by_value("Fox")
    print("List after removing all:")

    my_circular_list.show_list_forward()
