"""
思路：维护三个数组，[0,i),[i,j),[j,k]分别代表0,1,2的划分
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i,j=0,0
        for k in range(len(nums)):
            v = nums[k]
            nums[k]=2
            if v < 2:
                nums[j]=1
                j+=1
            if v < 1:
                nums[i] = 0
                i+=1
        
