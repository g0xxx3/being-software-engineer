# Python program to do inorder traversal without recursion


# A binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inOrderTraversal(root):
    current = root
    stack = []
    done = False
    while not done:
        if current:
            stack.append(current)
            current = current.left
        else:
            if len(stack):
                current = stack.pop()
                print(current.data)
                current = current.right
            else:
                done = True


node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)

inOrderTraversal(node)
