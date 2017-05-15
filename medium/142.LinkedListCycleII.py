"""
http://blog.csdn.net/xy010902100449/article/details/48995255
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        if head is None:return None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:break
        if fast == slow and fast.next:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return fast
        return None
            
