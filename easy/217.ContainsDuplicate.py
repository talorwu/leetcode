class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        Set = set()
        for num in nums:
            if num in Set:
                return True
            else:
                Set.add(num)
        return False
