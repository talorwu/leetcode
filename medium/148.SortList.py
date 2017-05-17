"""
思路：mergeSort
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.mergeSort(head)
        
    def mergeSort(self,head):
        if not head or not head.next:return head
        head1 = head
        head2 = self.getMid(head)
        head1 = self.mergeSort(head1)
        head2 = self.mergeSort(head2)
        return self.merge(head1,head2)
        
    def getMid(self,head):
        fast = slow = pre = head
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        pre.next = None
        return slow
        
    def merge(self,head1,head2):
        Head = newHead = ListNode(-1)
        while head1 and head2:
            if head1.val < head2.val:
                newHead.next = head1
                head1 = head1.next
            else:
                newHead.next = head2
                head2 = head2.next
            newHead = newHead.next
            
        if head1:
            newHead.next = head1
        if head2:
            newHead.next = head2
        return Head.next
            
            
            
        
        
        
        
        
