"""
思路：贪心
"""

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        step = 0
        i = 0
        while i < n:
            if i+nums[i] >= n-1:
                if i != n-1:return step+1
                else:return step
            next = i
            max = nums[i]
            for j in range(nums[i]+1):
                if max < j+nums[j+i]:
                    max =  j+nums[j+i]
                    next = i+j
            if next != i:
                step += 1
                i = next
        return step
