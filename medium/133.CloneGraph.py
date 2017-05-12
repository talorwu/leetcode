"""
思路：BFS+dic
"""

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:return None
        q = []
        dic = {}
        Node = UndirectedGraphNode(node.label)
        q.append(node)
        dic[node] = Node
        flag = 0
        while q:
            tmp = q.pop(0)
            for neighbor in tmp.neighbors:
                if neighbor not in dic:
                    Node1 = UndirectedGraphNode(neighbor.label)
                    dic[neighbor] = Node1
                    dic[tmp].neighbors.append(Node1)
                    q.append(neighbor)
                else:
                    dic[tmp].neighbors.append(dic[neighbor])
        return Node
                
                
