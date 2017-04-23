"""
思路：hashtable
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashtable = {}
        res = 0
        for i in range(len(nums))[::-1]:
            if nums[i] not in hashtable:
                hashtable[nums[i]] = 1
                res+=1
            elif hashtable[nums[i]] < 2:
                hashtable[nums[i]]+=1
                res+=1
            else:
                nums.remove(nums[i])
            
        return res
