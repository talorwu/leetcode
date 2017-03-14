"""
两种方法：
方法一：递归，// x* matches empty string or at least one character: x* -> xx*
            // *s is to ensure s is non-empty
方法二：DP
/**
         * f[i][j]: if s[0..i-1] matches p[0..j-1]
         * if p[j - 1] != '*'
         *      f[i][j] = f[i - 1][j - 1] && s[i - 1] == p[j - 1]
         * if p[j - 1] == '*', denote p[j - 2] with x
         *      f[i][j] is true iff any of the following is true
         *      1) "x*" repeats 0 time and matches empty: f[i][j - 2]
         *      2) "x*" repeats >= 1 times and matches "x*x": s[i - 1] == x && f[i - 1][j]
         * '.' matches any single character
         */
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p=="":return s==""
        if len(p) == 1:
            return p==s or (p=='.' and len(s) == 1)
        if p[1] == '*':
            return self.isMatch(s,p[2:]) or (s!="" and (p[0]==s[0] or p[0]=='.') and self.isMatch(s[1:],p))
        else:
            return s!="" and (s[0]==p[0] or p[0]=='.') and self.isMatch(s[1:],p[1:])


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        f=[[False]*(len(p)+1) for _ in range(len(s)+1)]
        f[0][0] = True
        for i in range(2,len(p)+1):
            f[0][i] = f[0][i-2] and p[i-1]=='*'
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1] != '*':
                    f[i][j] = f[i-1][j-1] and (s[i-1]==p[j-1] or p[j-1]=='.')
                else:
                    f[i][j] = f[i][j-2] or (f[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
        #print(f)
        return f[len(s)][len(p)]
