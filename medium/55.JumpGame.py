"""
思路：贪心。每次选择下次可以跳最远的地方
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:return True
        n = len(nums)
        i=0
        next=0
        while i<n:
            #print i
            if i+nums[i]>=n-1:return True
            
            next = i
            max = 0
            for j in range(nums[i]+1):
                if max < j+nums[i+j]:
                    max = j+nums[i+j]
                    next = i+j
            if i==next:return False
            i = next
