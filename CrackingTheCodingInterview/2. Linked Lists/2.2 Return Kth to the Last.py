# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

from random import randrange


class Node(object):
    def __init__(self, v):
        self.next = None
        self.value = v

def find_kth_element_from_end(head, k):
    fast_forward = head
    slow_forward = head

    for i in range(k):
        if not fast_forward:
            return False
        fast_forward = fast_forward.next

    while fast_forward:
        fast_forward = fast_forward.next
        slow_forward = slow_forward.next

    return slow_forward.value


if __name__ == '__main__':
    # Generate input data
    head = Node(3)
    current_node = head

    for i in range(10):
        v = randrange(1, 10)
        current_node.next = Node(v)
        current_node = current_node.next

    # Print input data
    current_node = head
    while current_node:
        print(current_node.value)
        current_node = current_node.next

    # Output result
    value = find_kth_element_from_end(head, 3)
    print(value)
