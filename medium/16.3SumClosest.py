"""
思路：和15.3SUM类似
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = target
        if len(nums) == 0:return res
        rrr = res = 99999
        nums_sort = sorted(nums)
        front = nums_sort[0]+1
        for i in range(len(nums)-2):
            if front == nums_sort[i]:
                continue
            front = nums_sort[i]
            tar = target-nums_sort[i]
            l = i+1;r = len(nums)-1;
            while(l < r):
                if nums_sort[l]+nums_sort[r] == tar:
                    return target 
                else:
                    if abs(tar - nums_sort[l] - nums_sort[r]) < res:
                        res = abs(tar - nums_sort[l] - nums_sort[r])
                        rrr = nums_sort[i] + nums_sort[l] +nums_sort[r] 
                    if nums_sort[l] + nums_sort[r] > tar:
                        r-=1
                    else:
                        l+=1
        return rrr
