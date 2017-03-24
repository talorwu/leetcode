"""
思路：二分搜索
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        p,l,r = -1,0,n-1
        while l<=r:
            mid = int((l+r)/2)
            if nums[mid] == target:p=mid;break
            elif nums[mid] > target:r = mid-1
            else:l = mid + 1
        if p == -1:return [-1,-1]
        l,r = 0,p
        while l<=r:
            mid = int((l+r)/2)
            if nums[mid] == target:r = mid-1
            else:l = mid+1
        left = r+1
        l,r = p,n-1
        if l==r:return [left,l]
        while l<=r:
            mid = int((l+r)/2)
            if nums[mid] == target:l=mid+1
            else:r = mid-1
        return [left,l-1]
            
