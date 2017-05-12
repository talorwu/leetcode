"""
思路：使用set
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums = set(nums)
        while nums:
            n = nums.pop()
            i = n+1
            l1,l2 = 0,0
            while i in nums:
                nums.remove(i)
                i+=1
                l1+=1
            i = n-1
            while i in nums:
                nums.remove(i)
                i-=1
                l2+=1
            res = max(res,l1+l2+1)
        return res
