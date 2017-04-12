"""
思路1：动态规划d
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == '':return s==''
        if s == '':return p=='*'*len(p)
        f=[[False]*(len(p)+1) for _ in range(len(s)+1)]
        f[0][0] = True
        for i in range(1,len(p)+1):
            f[0][i] = f[0][i-1] and p[i-1]=='*'
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='*':
                    f[i][j] = f[i][j-1] or f[i-1][j]
                elif p[j-1] == '?':
                    f[i][j] = f[i-1][j-1]
                else:
                    f[i][j] = f[i-1][j-1] and s[i-1]==p[j-1]
        #print f
        return f[i][j]
