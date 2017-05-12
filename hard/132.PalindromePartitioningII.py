
"""
Calculate and maintain 2 DP states:

    pal[i][j] , which is whether s[i..j] forms a pal

    d[i], which
    is the minCut for s[i..n-1]

Once we comes to a pal[i][j]==true:

    if j==n-1, the string s[i..n-1] is a Pal, minCut is 0, d[i]=0;
    else: the current cut num (first cut s[i..j] and then cut the rest
    s[j+1...n-1]) is 1+d[j+1], compare it to the exisiting minCut num
    d[i], repalce if smaller.

"""
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        f = [999999]*n #f[i]表示s[i:]的最小切割次数
        p = [[False]*n for _ in range(n)]
        for i in range(n):
            p[i][i] = True
            
        for i in range(n)[::-1]:
            f[i] = n-i-1
            for j in range(i,n):
                p[i][j] = s[i]==s[j] and (j-i<2 or p[i+1][j-1])
                if p[i][j]:
                    if j == n-1:
                        f[i] = 0
                    else:
                        f[i] = min(f[i],f[j+1]+1)
        return f[0]
                    

                
                
                
