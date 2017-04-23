"""
思路：hashtable
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
        hashtable = {}
        p=ListNode(0)
        p.next = head
        p1 = p
        while p.next:
            if p.next.val not in hashtable:
                hashtable[p.next.val] = 1
            else:
                hashtable[p.next.val] += 1
            p = p.next
        p = p1
        while p.next:
            if hashtable[p.next.val] > 1:
                p.next = p.next.next
            else:
                p=p.next
        return p1.next
            
