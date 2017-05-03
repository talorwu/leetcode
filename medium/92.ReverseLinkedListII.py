"""
思路：
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        p = ListNode(0)
        p.next = head
        left = right =  p
        for _ in range(m-1):
            left = left.next
        for _ in range(n):
            right = right.next
        while left.next != right:
            tmp = left.next
            left.next = tmp.next
            tmp.next = right.next
            right.next = tmp
            #left = left.next
        return p.next
            
            
            
            
            
        
