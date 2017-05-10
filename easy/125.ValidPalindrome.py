class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = s.lower()
        
        ss = [v for v in s if v.isalpha() or v.isdigit()]
        if ss == []:return True
        i,j = 0,len(ss)-1
        #print ss
        while i<=j:
            # s[i],s[j]
            if ss[i]!=ss[j]:return False
            i+=1
            j-=1
        return True
