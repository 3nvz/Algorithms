
#inorder
# left subtree, root, right subtree

#preorder
# root, left subtree, right subtree

#postorder
# left subtree, right subtree, root


class Node:
    
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item

def inorder(root):
        
    if root:
        inorder(root.left)
        print(str(root.val))
        inorder(root.right)


def preorder(root):
    if root:
        print(str(root.val))
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val))
    
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal ")
inorder(root)

print("\nPreorder traversal ")
preorder(root)

print("\nPostorder traversal ")
postorder(root)