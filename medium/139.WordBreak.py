"""
思路：DP f[i]表示s[0:i)是否可以word break
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        f = [False] * (len(s)+1)
        f[0] = True
        for i in range(1,len(s)+1):
            for j in range(0,i):
                if f[j] and s[j:i] in wordDict:
                    f[i] = True
                    break
        #print f
        return f[len(s)]
