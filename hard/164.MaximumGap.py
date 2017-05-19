"""
思路：1.基数排序
      2.桶排序
解题报告：https://leetcode.com/articles/maximum-gap/#approach-1-comparison-sorting-accepted
"""

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <2:return 0
        exp = 1
        count = [0] * 10
        maxVal = max(nums)
        aux = [0]*len(nums)
        while maxVal / exp > 0:
            count = [0] * 10
            for i in range(len(nums)):
                count[nums[i] / exp %10] += 1
            for i in range(1,len(count)):
                count[i]+=count[i-1]
            for i in range(len(nums))[::-1]:  #倒序为了稳定性，单次没有关系，但是多次排序必须倒序
                count[nums[i]/exp%10] -= 1
                aux[count[nums[i]/exp%10]] = nums[i]
            for i in range(len(nums)):
                nums[i] = aux[i]
            exp*=10
        maxGap = 0
        #print nums
        for i in range(1,len(nums)):
            maxGap = max(maxGap,nums[i]-nums[i-1])
        return maxGap
            


#桶排序
     if len(nums) < 2:return 0
        minn = min(nums)
        maxx = max(nums)
        bucketSize = max(1,(maxx - minn)/(len(nums)-1))
        bucketNum = (maxx - minn)/bucketSize + 1
        buckets = [bucket() for _ in range(bucketNum)]
        #print bucketSize,bucketNum
        for num in nums:
            bucketId  = (num - minn)/bucketSize
            #print bucketId
            buckets[bucketId].used = True
            buckets[bucketId].minVal = min(num,buckets[bucketId].minVal)
            buckets[bucketId].maxVal = max(buckets[bucketId].maxVal,num)
            #print bucketId, buckets[bucketId].minVal, buckets[bucketId].maxVal
        preBucketMax = minn
        maxGap = 0
        for buc in buckets:
            if not buc.used:
                continue
            #print buc.minVal,buc.maxVal
            maxGap = max(maxGap, buc.minVal - preBucketMax)
            preBucketMax = buc.maxVal
        return maxGap
            
            
            
