"""
拓扑排序
"""

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        edges = [[] for _ in range(numCourses)]
        
        indegree = [0]*numCourses
        for x,y in prerequisites:
            edges[y].append(x)
            indegree[x] += 1
        res = []
        q = []
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            course = q.pop(0)
            res.append(course)
            for x in edges[course]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    q.append(x)
            
        return res if len(res) == numCourses else []
            
            
            
            
            
