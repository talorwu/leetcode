"""
思路：先二分查找最小的值，然后二分搜索
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0 :return -1
        l,r = 0,n-1
        while l<r:
            mid = int((l+r)/2)
            if nums[mid]>=nums[0]:l=mid+1
            else:r=mid
        if nums[l]<nums[0]:
            p = l
        else:
            p=n
        
        if target >= nums[0]:l,r = 0,p-1
        else :l,r = p,n-1
        while l<r:
            mid = int((l+r)/2)
            if nums[mid] == target:return mid
            if nums[mid] > target:r = mid
            else:l=mid+1
        if nums[r] == target:return l
        return -1
