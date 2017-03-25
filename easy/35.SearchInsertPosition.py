class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0, len(nums)-1
        while l<=r:
            mid = int((l+r)/2)
            if nums[mid] == target:return mid
            elif nums[mid]<target:l=mid+1
            else: r=mid-1
        return l
