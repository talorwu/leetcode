"""
暴力解法，从左到右一次比较，还有一种解法说，先排序，然后比较最后一个和第一个，但是复杂度更高
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        res = strs[0]
        for i in range(1,len(strs)):
            res = self.commonPrefix(res , strs[i])
        return res
        
        
    def commonPrefix(self , s1,s2):
        i=0
        minlen = min(len(s1),len(s2))
        while i < minlen:
            if s1[i]==s2[i]:
                i+=1
            else:
                break
        return s1[:i]
