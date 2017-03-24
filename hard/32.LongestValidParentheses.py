"""
思路：方法1：使用stack，保存未匹配的括号，然后寻找最大的匹配长度
      方法2：dp,dp[i]表示以i为结尾的最长的匹配长度
      方法3：两个指针，分别表示(和)的个数，从左到右，从右到左各扫一遍
"""
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = []
        for i in range(len(s)):
            if s[i]=='(':
                L.append(i)
            elif len(L)!=0 and s[L[-1]] == '(':
                L.pop()
                #print(L)
            else:
                L.append(i)
        res = 0
        #print(L)
        if len(L)==0:return len(s)
        l,r = 0,len(s)
        while len(L):
            l = L.pop()
            res = max(res,r-l-1)
            r = l
        res = max(res , l)
        return res

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        n = len(s)
        dp = [0]*n
        for i in range(1,n):
            if s[i]==')' and s[i-1]=='(':
                dp[i] = dp[i-2]+2
            elif s[i]==')' and s[i-1] == ')' and i-dp[i-1]-1 >=0 and s[i-dp[i-1]-1] == '(':
                dp[i] = dp[i-1]+dp[i-dp[i-1]-2]+2
            res = max(res,dp[i])
        #print(dp)
        return res

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l,r,res= 0,0,0
        for c in s:
            if c == '(':l+=1
            else:r+=1
            if l==r:res = max(res,l*2)
            elif r>l:l,r=0,0
        l,r = 0,0
        n = len(s)-1
        while n >= 0:
            if s[n] == '(':l+=1
            else:r+=1
            if l==r:res = max(res,l*2)
            elif l>r:l,r=0,0
            n-=1
        return res
                
