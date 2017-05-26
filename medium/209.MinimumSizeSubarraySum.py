"""
思路：O(2n)算法
"""

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i = j = 0
        res = len(nums)+1
        summ = 0
        while j<len(nums):
            summ += nums[j]
            while summ >= s:
                summ -= nums[i]
                i += 1
                res = min(res,j-i+2)
            #print res,i,j
            j+=1
        return res if res <=len(nums) else 0
