class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        for i in range(len(digits))[::-1]:
            if i==len(digits)-1:
                digits[i] +=1
                carry = digits[i]/10
                digits[i]%=10
            else:
                digits[i]+=carry
                carry = digits[i]/10
                digits[i]%=10
        print digits
        res = [-1]*(len(digits)+1)
        for i in range(1,len(res)):
            res[i] = digits[i-1]
        if carry > 0:
            res[0]=carry
        else:
            res.remove(-1)
        return res
