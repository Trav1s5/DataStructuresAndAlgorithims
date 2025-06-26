class TreeNode:

    def __init__(self, value):
        self.left=None
        self.right=None
        self.value=value

    def insert(self,key):
        #goes left or right
        if key < self.value: #LEFT SIDE
            if self.left is None: #checks if left side is empty if it is  this runs:
                self.left = TreeNode(key) #there will be insertion on the left side
            else:  # recursive call our method till we find a null
                self.left.insert(key)

        elif key > self.value: #RIGHT SIDE
            if self.right is None:
                self.right = TreeNode(key)
            else:#recursive call our method till we find a null
                self.right.insert(key)

    def find(self,key):

       if key < self.value:

           if self.left is None:
               return False
           else:
               return self.left.find(key)

       elif key > self.value:

           if self.right is None:
               return False
           else:
               return self.right.find(key)
       else:
           return True


    def preorder_traversal(self):
        print(self.value)

        if self.left:
            self.left.inorder_traversal()

        if self.right:
            self.right.inorder_traversal()


    def inorder_traversal(self):
        # inorder print is in between
       if self.left:
           self.left.postorder_traversal()

       print(self.value)

       if self.right:
           self.right.postorder_traversal()


    def postorder_traversal(self):
        # postorder print comes as the last one
        if self.left:
            self.left.postorder_traversal()

        if self.right:
            self.right.postorder_traversal()

        print(self.value)


if __name__ == "__main__":

    tree = TreeNode(10)#parent node

    tree.insert(5)
    tree.insert(3)
    tree.insert(4)
    tree.insert(11)
    tree.insert(12)
    tree.insert(13)


    print("\n preorder_traversal")
    tree.preorder_traversal()

    print("\n inorder_traversal")
    tree.inorder_traversal()

    print("\n postorder_traversal")
    tree.postorder_traversal()
