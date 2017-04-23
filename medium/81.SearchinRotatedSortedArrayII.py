"""
思路：第一步，寻找第一个比nums[0]小的元素，如果找的位置在Len(nums)位置，则需要向前寻找
      第二步，二分查找
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums)==0:return False
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)/2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid -1
        rotate = l
        #print rotate,len(nums)
        if rotate == len(nums):
            rotate -=1
            while rotate != 0 and nums[rotate]==nums[0]:
                rotate -=1
            if nums[rotate] > nums[0]:
                rotate += 1
        #print rotate
        #if rotate == 0 or rotate == len(nums):
        l,r = 0,rotate-1
        while l<=r:
            mid = (l+r)/2
            if target == nums[mid]:
                return True
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        l,r = rotate,len(nums)-1
        while l<=r:
            mid = (l+r)/2
            if target == nums[mid]:
                return True
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False
            
