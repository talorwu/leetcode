"""
思路：1.拓扑排序
      2.DFS，必须使用邻接表，使用邻接矩阵会超时，https://discuss.leetcode.com/topic/13412/python-20-lines-dfs-solution-sharing-with-explanation
"""
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if len(prerequisites) <= 1:return True
        edges = [[0]*numCourses for _ in range(numCourses)]
        indegree = [0]*numCourses
        for i in range(len(prerequisites)):
            edges[prerequisites[i][1]][prerequisites[i][0]] = 1
            indegree[prerequisites[i][0]] += 1
        
        q = []
        count = 0
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            course = q.pop(0)
            count += 1
            for i in range(numCourses):
                if edges[course][i] == 1:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        q.append(i)
        return count == numCourses
            
            
            
            
            
        #DFS
        if len(prerequisites) <= 1:return True
        edges = [[] for _ in xrange(numCourses)]
        visited = [0 for _ in xrange(numCourses)]
        for x, y in prerequisites:
            edges[y].append(x)
        for i in range(numCourses):
            if not self.findCycle(edges,i,visited):return False
        return True
        
    def findCycle(self,edges,node,visited):
        if visited[node] == 1:
            return True
        if visited[node] == -1:
            return False
        visited[node] = -1
        for i in edges[node]:
            if not self.findCycle(edges,i,visited):
                return False
        visited[node] = 1
        return True    
