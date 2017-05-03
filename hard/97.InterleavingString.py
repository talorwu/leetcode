"""
思路：DP,f[i,j]表示s1[0:i]和s2[0:j]能否组成s3[0:i+j]
"""
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        len1,len2,len3 = len(s1),len(s2),len(s3)
        if len1+len2 != len3 : return False
        f = [[False]*(len2+1) for _ in range(len1+1)]
        f[0][0] = True
        for i in range(1,len1+1):
            f[i][0] = f[i-1][0] and s1[i-1] == s3[i-1]
        for i in range(1,len2+1):
            f[0][i] = f[0][i-1] and s2[i-1] == s3[i-1]
        
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                f[i][j] = (s1[i-1]==s3[i+j-1] and f[i-1][j]) or (s2[j-1]==s3[i+j-1] and f[i][j-1])
        return f[len1][len2]
