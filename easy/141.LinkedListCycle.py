"""
题目要求是判断链表是否有环，leetcode上链表的题都是没有头结点的，这点大家要记住。而且若链表有环，也是最后一个节点形成的环。

大家考虑这样一个问题，链表的环相当于一个圆形操场。假设有两个人在圆形操场上无限循环的跑，那么速度快的一定能追得上速度慢的。同理，若要判断一个链表是否有环，可设计快慢指针，当快慢指针都进入环的时候，若最终两个指针相遇，必可说明链表存在环。下面就要考虑快慢指针的步长，从跑操场的情况来看，不管慢的有多慢，快得有多快，最终肯定能相遇。同理，链表中，也可随意指定快慢指针的步长，无非就是跑的圈数多少的问题。 
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:return False
        fast = head
        slow = head
        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:return True
        return False
