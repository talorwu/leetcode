"""
思路：吧所有的数放在正确的位置，比如3，放在nums[3]的位置
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[i]!=nums[nums[i]-1]:
                print i , nums[i]-1
                self.swap(nums,i,nums[i]-1)
        for i in range(n):
            if nums[i] != i+1:return i+1
        return n+1
    def swap(self,a,i,j):
        t = a[i]
        a[i] = a[j]
        a[j] = t
        
