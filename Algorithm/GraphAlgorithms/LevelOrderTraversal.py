from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def traverse_level(root):
    if root:
        queue = deque([root])
        while len(queue):
            item = queue.popleft()
            print(item.data)
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
    pass


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
    traverse_level(root)

    print('')
    print('')
    print('')

    root = Node(2)
    root.right = Node(9)
    root.right.left = Node(8)
    root.right.left.left = Node(6)
    root.right.right = Node(7)
    traverse_level(root)