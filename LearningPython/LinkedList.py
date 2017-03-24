# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c = 0
        output = None
        p = None
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            v = v1 + v2 + c
            if v > 9:
                v -= 10
                c = 1
            else:
                c = 0

            l = ListNode(v)
            if not output:
                output = p = l
            else:
                p.next = l
                p = l
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if c == 1:
            l = ListNode(c)
            p.next = l

        return output


input_list_1 = None
input_list_2 = None

prev = None
for n in [2, 4, 3, 4]:
    l = ListNode(n)

    if not input_list_1:
        input_list_1 = prev = l
    else:
        prev.next = l
        prev = l

prev = None
for n in [5, 6, 4, 6]:
    l = ListNode(n)

    if not input_list_2:
        input_list_2 = prev = l
    else:
        prev.next = l
        prev = l

s = Solution()
a = s.addTwoNumbers(input_list_1, input_list_2)
print(a)