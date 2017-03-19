"""
思路：排序，然后固定第一个数字，剩下的就是2Sum问题， O(n**2)算法
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums_sort = sorted(nums)
        if len(nums) == 0:return res
        front = nums_sort[0]+1
        for i in range(len(nums)-2):
            if front == nums_sort[i]:
                continue
            front = nums_sort[i]
            target = -nums_sort[i]
            l = i+1;r = len(nums)-1;
            while(l < r):
                if nums_sort[l]+nums_sort[r] == target:
                    res.append([nums_sort[i] , nums_sort[l], nums_sort[r]])
                    while l+1 < len(nums) and nums_sort[l]==nums_sort[l+1]:
                        l+=1
                    while r-1 > i and nums_sort[r]==nums_sort[r-1]: 
                        r-=1
                    l+=1;r-=1
                else:
                    if nums_sort[l] + nums_sort[r] > target:
                        r-=1
                    else:
                        l+=1
        return res
