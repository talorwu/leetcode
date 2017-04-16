"""
思路：DP，f[i]表示以nums[i]结尾的最大的值，if f[i-1]>0:f[i] = f[i-1]+nums[i];else:f[i] = nums[i]
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        f = [0]*n
        f[0] = nums[0]
        res = f[0]
        for i in range(1,n):
            if f[i-1] > 0:
                f[i] = f[i-1]+nums[i]
            else:
                f[i] = nums[i]
            res = max(res,f[i])
        return res
