"""
思路：按照搞定度加法处理
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i=len(a)-1
        j=len(b)-1
        res = [0]*(max(i,j)+2)
        k=0
        carry=0
        while i>=0 and j>=0:
            res[k] = (int(a[i])+int(b[j])+carry)%2
            carry = (int(a[i])+int(b[j])+carry)/2
            i-=1
            j-=1
            k+=1
        while i>=0:
            res[k] = (int(a[i])+carry)%2
            carry = (int(a[i])+carry)/2
            i-=1
            k+=1
        while j>=0:
            res[k] = (int(b[j])+carry)%2
            carry = (int(b[j])+carry)/2
            j-=1
            k+=1
        res[k]+=carry
        res.reverse()
        res1 = [str(x) for x in res]
        #print res,carry
        if carry:return ''.join(res1)
        else:return ''.join(res1[1:])
        
