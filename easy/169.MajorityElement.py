"""
主要是more than,就是严格大于的意思
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = nums[0]
        count = 1
        for i in nums[1:]:
            if count == 0:
                count+=1
                major = i
            elif i == major:
                count+=1
            else:
                count -=1
        return major
