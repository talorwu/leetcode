"""
思路：1.暴力，2.KMP
"""
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s
            
        


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # r = s[::-1]
        # for i in range(len(s) + 1):
        #     if s.startswith(r[i:]):
        #         return r[:i] + s
            
        #KMP
        A = s+'#'+s[::-1]
        #get lookup table
        table = [0]*len(A)
        #pointer that points to matched char in prefix part
        index = 0
        #skip index 0, we will not match a string with itself
        for i in range(1,len(A)):
            #we can extend match in prefix and postfix
            if A[i] == A[index]:
                table[i] = table[i-1]+1
                index+=1
            else:
                #match failed, we try to match a shorter substring
                #by assigning index to table[i-1], we will shorten the match string length, and jump to the 
                #prefix part that we used to match postfix ended at i - 1
                index = table[i-1]
                while index>0  and A[i]!=A[index]:
                    index = table[index-1]
                #when we are here may either found a match char or we reach the boundary and still no luck
                #so we need check char match
                if A[i] == A[index]:
                    index += 1
                table[i] = index
                
                
                
        return s[table[-1]:][::-1]+s
                
