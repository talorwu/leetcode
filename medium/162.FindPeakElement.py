"""
思路：二分
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)/2
            if mid ==0 or nums[mid] > nums[mid-1]:
                l = mid + 1
            else:
                r = mid - 1
        return l-1
