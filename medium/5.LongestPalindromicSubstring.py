"""
思路：从中间往两边拓展，依次寻找最长回文子串，回文串中心从(a[0],a[0]a[1]),(a[1],a[1]a[2])...(a[n-2],a[n-2]a[n-1])
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        
        for i in xrange(len(s)):
            tmp = self.palindrome(s,i,i)
            if len(tmp) >= len(res):
                res = tmp
            tmp = self.palindrome(s,i,i+1)
            if len(tmp) >= len(res):
                res = tmp
        return res
    def palindrome(self,s,l,r):
        while l>=0 and r<len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return s[l+1:r]
            
