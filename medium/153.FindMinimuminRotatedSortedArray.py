
"""
思路：二分
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)/2
            if mid-1<0 or nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1
        if l >= len(nums):return nums[0]
        return nums[l]
