"""
思路:两个指针，注意处理k>len的情况
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if not head:return head
        p = head
        len = 0
        while p:
            len+=1
            p=p.next
        k%=len
        h = ListNode(0)
        h.next = head
        p,f = h,h
        while k>0:
            p=p.next
            k-=1
        while p.next:
            p=p.next
            f=f.next
        p.next = h.next
        h.next = f.next
        f.next=None
        return h.next
        
        
        
