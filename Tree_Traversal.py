#Node Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Inoder
def Inorder(Root):
    if Root:
        Inorder(Root.left)
        print(Root.data)
        Inorder(Root.right)

#Preorder
def Preorder(Root):
    if Root:
        print(Root.data)
        Preorder(Root.left)
        Preorder(Root.right)

#Postorder
def Postorder(Root):
    if Root:
        Postorder(Root.left)
        Postorder(Root.right)
        print(Root.data)

#Height of the tree
def height(Root):
    if Root is None:
        return 0
    return 1 + max(height(Root.left), height(Root.right))

Root = Node(1)
Root.left = Node(2)
Root.right = Node(3)
Root.left.left = Node(4)
Root.left.right = Node(5)
Root.right.right = Node(6)
Root.left.left.left = Node(7)
Root.right.left = Node(8)

#Output
print("Inorder:")
Inorder(Root)
print("\nPreorder:")
Preorder(Root)
print("\nPostorder:")
Postorder(Root)

print("\nHeight of tree:", height(Root))
