from collections import defaultdict


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def vertical_sum(node, vertical_index_dict, index):
    if vertical_index_dict[index]:
        vertical_index_dict[index] = vertical_index_dict[index] + node.data
    else:
        vertical_index_dict[index] = node.data

    if node.left:
        vertical_sum(node.left, vertical_index_dict, index - 1)
    if node.right:
        vertical_sum(node.right, vertical_index_dict, index + 1)


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
    vertical_index = defaultdict(int)
    vertical_sum(root, vertical_index, 0)
    print(vertical_index)

    print('')
    print('')
    print('')

    root = Node(2)
    root.right = Node(9)
    root.right.left = Node(8)
    root.right.left.left = Node(6)
    root.right.right = Node(7)
    vertical_index = defaultdict(int)
    vertical_sum(root, vertical_index, 0)
    print(vertical_index)
