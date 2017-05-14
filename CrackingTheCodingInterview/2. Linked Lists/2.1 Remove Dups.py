# Remove Dups! Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP - How would you solve this problem if a temporary buffer is not allowed?
from random import randrange


class Node(object):
    def __init__(self, v):
        self.next = None
        self.value = v

def delete_dups(node):
    if not node and not node.next:
        return node

    visited_items = set()
    previous_node = node
    current_node = node.next
    visited_items.add(node.value)
    while current_node:
        if current_node.value in visited_items:
            previous_node.next = current_node.next
        else:
            visited_items.add(current_node.value)
            previous_node = current_node

        current_node = current_node.next

    return node

if __name__ == '__main__':
    head = Node(3)
    current_node = head
    for i in range(10):
        v = randrange(1, 10)
        current_node.next = Node(v)
        current_node = current_node.next
    head = delete_dups(head)

    current_node = head
    while current_node:
        print(current_node.value)
        current_node = current_node.next
