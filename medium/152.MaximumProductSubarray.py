class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        imax = imin = res
        for i in range(1,len(nums)):
            if nums[i] < 0:
                tmp = imax
                imax = imin
                imin = tmp
            imax = max(imax*nums[i],nums[i])
            imin = min(imin*nums[i],nums[i])
            res = max(res,imax)
        return res
        
        
        
        
