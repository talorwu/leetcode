"""
递归
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:return "1"
        tmp = self.countAndSay(n-1)
        tmp+='#'
        i=0
        l = 1
        res = ""
        print(tmp)
        while i<len(tmp)-1:
            if(tmp[i]==tmp[i+1]):
                l+=1;i+=1
            else:
                res+=(str(l)+tmp[i])
                i+=1
                l=1
        return res
                
            
        
                
                
                
            
