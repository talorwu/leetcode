"""
通用解法：https://discuss.leetcode.com/topic/11877/detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers/2

"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x1,x2,mask = 0,0,0
        for i in nums:
            x2 ^= (x1 & i)
            x1 ^= i
            mask = ~(x1 & x2);
            x2 &= mask;
            x1 &= mask;
        return x1
