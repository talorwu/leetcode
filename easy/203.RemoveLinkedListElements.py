# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        Head = ListNode(0)
        Head.next = head
        p = Head
        while p:
            if p.next and p.next.val == val:
                p.next = p.next.next
            else:p=p.next
        return Head.next
