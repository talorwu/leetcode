# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        f,s=l1,l2
        h = newList=ListNode(0)
        while f and s :
            if f.val <= s.val:
                newList.next = f;f=f.next
            else : 
                newList.next = s;s=s.next
            newList = newList.next
        if f:
            newList.next = f;
        else:
            newList.next = s;
            
        return h.next
                
