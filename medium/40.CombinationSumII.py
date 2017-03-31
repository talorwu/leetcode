"""
思路：同样DFS，在枚举第一个元素的时候，遇到相等的元素直接跳过
"""
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res =[]
        self.DFS(candidates,target,[],res)
        return res
    def DFS(self,c,target,result,res):
        if target == 0:
            res.append(result)
            return
        if len(c) == 0:return
        if target < c[0]:
            return
        i=0
        while i<len(c):
            x = c[i]
            if target >= x:
                self.DFS(c[i+1:],target-x,result+[x],res)
            while i+1<len(c) and c[i]==c[i+1]:i+=1
            i+=1

        
