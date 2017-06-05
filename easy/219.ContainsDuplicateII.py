"""
思路：hash
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = [i]
            else:
                dic[nums[i]].append(i)
        for v in dic.values():
            if len(v) > 1:
                for i in range(len(v)-1):
                    if v[i+1] - v[i] <= k:return True
        return False
                
