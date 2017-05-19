"""
找到长度差就可以了
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        while p1 and p2:
            if p1 == p2:return p1
            else:
                p1 = p1.next
                p2 = p2.next
        if not p1 and not p2:return None
        p11 = headA
        p21 = headB
        while p1:
            p11 = p11.next
            p1 = p1.next
        while p2:
            p21 = p21.next
            p2 = p2.next
        while p11 and p21:
            if p11 == p21:return p11
            else:
                p11 = p11.next
                p21 = p21.next
        return None
            
            
            
            
            
            
            
