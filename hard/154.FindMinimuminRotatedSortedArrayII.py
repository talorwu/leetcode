"""
认真处理l == len(nums)
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0,len(nums)-1
        # if nums[l] == nums[r]:return nums[0]
        while l<=r:
            mid = (l+r)/2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid - 1
        if l == len(nums) and nums[l-1] > nums[0]:
            return nums[0]
        elif l == len(nums):
            l-=1
            while l > 0 and nums[l] == nums[0]:
                l-=1
        if nums[l] > nums[0]:return nums[0]
        return nums[l]
