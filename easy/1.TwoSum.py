#复杂度O(n)算法
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for a in nums:
            
            b = target - a
            print(a,b)
            asub = nums.index(a)
            
            if b in nums:
               bsub = nums.index(b)
               if a == b:
                   nums[asub] = '0'
                   if b in nums:
                       bsub = nums.index(b)
                       #print(asub,bsub)
                       return [asub,bsub]
                   nums[asub] = a
               else:
                   return [asub,bsub]

#O(1)算法
"""
思路：使用dict记录target-nums[i]的值与小标，在这个dict中查找是否后面的nums[i]出现，如果出现说明dict表中的该元素对应的nums[k]与该nums[i]相加等于target
"""
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
                
    
