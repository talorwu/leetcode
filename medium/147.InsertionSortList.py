# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head : return None
        newHead = p = ListNode(-999999)
        while head:
            p = newHead
            while p.next and p.next.val < head.val:
                p = p.next
            tmp1 = head.next
            tmp = p.next
            p.next = head
            head.next = tmp
            head = tmp1
        return newHead.next
