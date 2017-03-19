"""
思路：用两个指针，一个指针先跑n+1步，然后剩下（length-n）步。所以当这个指针跑到最后的时候，第二个指针刚好跑到倒数n+1个
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        h = ListNode(0)
        h.next = head
        left ,right= h,h
        for i in range(n+1):
            left = left.next
        while left:
            left = left.next
            right = right.next
        right.next = right.next.next
        return h.next
            
