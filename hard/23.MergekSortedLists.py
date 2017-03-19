"""
思路：
1.分治
2.优先队列
3.heapq(最小堆)
"""




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        L = lists
        if len(L) == 0 : return []
        while len(L)>1:
            tmpL = []
            i=0
            while i < len(L)-1:
                l1,l2 = L[i],L[i+1]
                h = h1 = ListNode(0)
                while l1 and l2:
                    if l1.val <= l2.val:
                        h.next = l1
                        l1 = l1.next
                    else:
                        h.next = l2
                        l2 = l2.next
                    h = h.next
                if l1:h.next = l1
                if l2:h.next = l2
                tmpL.append(h1.next) 
                i+=2
            if len(L) % 2:tmpL.append(L[len(L)-1])
            L = tmpL
        return L[0]

###
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        q = PriorityQueue()
        for node in lists:
            if node: q.put((node.val,node))
        L =L1 = ListNode(None)
        while q.qsize():
            L.next = q.get()[1]
            L = L.next
            if L.next:q.put((L.next.val,L.next))
        return L1.next
                
        
                
                
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = [(node.val,node) for node in lists if node]
        heapq.heapify(h)
        L = L1 = ListNode(None)
        while h:
            L.next = heapq.heappop(h)[1]
            L = L.next
            if L.next:heapq.heappush(h,(L.next.val,L.next))
        return L1.next
                              
                
                
