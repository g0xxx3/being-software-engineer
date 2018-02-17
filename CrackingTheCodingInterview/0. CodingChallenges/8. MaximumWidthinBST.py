class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maximum_width(root_node):
    queue = []
    max_width = 0
    queue.append(root_node)
    while len(queue):
        if len(queue) > max_width:
            max_width = len(queue)
        frontier = []
        for node in queue:
            if node.left:
                frontier.append(node.left)
            if node.right:
                frontier.append(node.right)
        queue = frontier
    return max_width


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
    print(maximum_width(root))

    print('')
    print('')
    print('')

    root = Node(2)
    root.right = Node(9)
    root.right.left = Node(8)
    root.right.left.left = Node(6)
    root.right.right = Node(7)
    print(maximum_width(root))
