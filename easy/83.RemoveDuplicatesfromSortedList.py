"""
思路：set就可以了
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = set()
        p = ListNode(0)
        p.next = head
        p1 = p
        while p.next:
            if p.next.val not in s:
                s.add(p.next.val)
                p = p.next
            else:
                p.next = p.next.next
            #p = p.next
        return p1.next
