# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dic={}
        if head is None:return None
        q = []
        q.append(head)
        headCopy = RandomListNode(head.label)
        dic[head] = headCopy
        while q:
            tmp = q.pop(0)
            if tmp.next not in dic and tmp.next:
                nextCopy = RandomListNode(tmp.next.label)
                dic[tmp.next] = nextCopy
                dic[tmp].next = nextCopy
                q.append(tmp.next)
            elif tmp.next is None:
                dic[tmp].next = None
            else:
                dic[tmp].next = dic[tmp.next]
            if tmp.random not in dic and tmp.random:
                nextCopy = RandomListNode(tmp.random.label)
                dic[tmp.random] = nextCopy
                dic[tmp].random = nextCopy
                q.append(tmp.random)
            elif tmp.random is None:
                dic[tmp].random = None
            else:
                dic[tmp].random = dic[tmp.random]
        return headCopy
                
                
                
                
                
                
                
                
