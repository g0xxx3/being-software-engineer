# https://www.geeksforgeeks.org/boundary-traversal-of-binary-tree/


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getLeftBoundaryNodes(node):
    if node and node.data:
        print(node.data)
        getLeftBoundaryNodes(node.left)
    pass


def getLeafNodes(node):
    if node and node.data:
        getLeafNodes(node.left)
        if node.left is None and node.right is None:
            print(node.data)
        getLeafNodes(node.right)
    pass


def getRightBoundaryNodes(node):
    if node and node.data:
        getRightBoundaryNodes(node.right)
        print(node.data)
    pass


def getBoundaryNodes(node):
    traverse(node)

    print("")
    print("")
    if node and node.data:
        getLeftBoundaryNodes(node)
        getLeafNodes(node.left)
        getLeafNodes(node.right)
        getRightBoundaryNodes(node)
    pass


def traverse(node):
    if node and node.data:
        print(node.data)
        traverse(node.left)
        traverse(node.right)




if __name__ == '__main__':
    root = Node(2)
    root.left = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.left.left.right = Node(4)
    root.right = Node(9)
    root.right.left = Node(8)
    root.right.left.left = Node(6)
    root.right.right = Node(7)
    traverse(root)
    # getBoundaryNodes(root)

    print('')
    print('')
    print('')

    root = Node(2)
    root.right = Node(9)
    root.right.left = Node(8)
    root.right.left.left = Node(6)
    root.right.right = Node(7)
    traverse(root)
    # getBoundaryNodes(root)
