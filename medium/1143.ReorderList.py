"""
思路：先使用快慢指针将链表从中间分割成两段，然后后半段就地逆置．之后合并插入到前半段链表即可
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:return
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        fast1 = fast = slow.next
        pre = None
        #print fast.val
        while fast:
            #print fast.val
            tmp = fast.next
            fast.next = pre
            pre = fast
            fast = tmp
        slow.next = None
        slow = head
        fast = pre
        while fast:
            #print slow.val,fast.val
            tmp1 = slow.next
            tmp2 = fast.next
            slow.next = fast
            fast.next = tmp1
            slow = tmp1
            fast = tmp2
        #return head
            
            
            
        
