"""
思路：
DFS+剪枝
"""
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        results = []
        if len(s) > 12:return results
        self.DFS(s,[],results)
        res = []
        for r in results:
            res.append('.'.join(r))
        return res
    def DFS(self,s,res,results):
        if len(res) == 4 and s == '':
            results.append(res)
        for i in range(min(len(s),3)):
            if i==0 or (s[0] != '0' and int(s[:i+1]) <= 255):
                self.DFS(s[i+1:],res+[s[:i+1]],results)

