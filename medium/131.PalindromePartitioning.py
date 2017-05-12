"""
思路：DFS
"""
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self.DFS(s,[],result)
        return result
        
    def DFS(self,s,res,result):
        if s == "":
            result.append(res)
            return
        for i in range(1,len(s)+1):
            if self.check(s[:i]):
                self.DFS(s[i:],res+[s[:i]],result)
    def check(self,s):
        i,j=0,len(s)-1
        while i < j:
            if s[i]!=s[j]:return False
            i+=1
            j-=1
        return True
