class Node:
    def __init__(self , value):
        self.value = value
        self.left =None
        self.right = None

def insert (root , value):
    if root is None:
        return Node (value)
    if value < root.value:
        root.left = insert(root.left , value)
    else:
        root.right = insert(root.right , value)
    return root

def recursive_search (root, key_value):
    if root is None:
        return None
    if root.value == key_value:
        return root
    elif key_value < root.value:
        return recursive_search(root.left , key_value)
    else:
        return recursive_search(root.right ,key_value)

if __name__ == '__main__':
    values= [10,20,30,40,50,60,70,80,90]
    binarySearchTree_root = None
    for values in values:
        binarySearchTree_root = insert(binarySearchTree_root , values)

    target = 90
    result = recursive_search(binarySearchTree_root , target)
    if result:
        print(f"Found:{result.value}")
    else:
        print("Value not found")

