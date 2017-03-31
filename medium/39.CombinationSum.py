"""
思路：DFS，枚举开始的位置
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort(reverse=True)
        res = []
        self.DFS(candidates,target,[],res)
        return res
        
    def DFS(self,c,target,result,res):
        
        if target == 0:
            res.append(result)
            return
        if target < c[len(c)-1]:return

        for i in range(len(c)):
            x = c[i]
            if target >= c[i]:
                self.DFS(c[i:],target-x,result+[x],res)
            
        
