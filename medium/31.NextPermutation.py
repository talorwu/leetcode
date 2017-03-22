"""
思路：查找第一个nums[i]>nums[i-1],找到这个i之后，再找i～n-1中最小的大于nums[i-1]的数,然后交换这两个值，然后i~n-1按从小到大排序即可
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n==1:return
        i = n-1
        while i>0 and nums[i]<=nums[i-1]:i-=1
        i-=1
        #print(i)
        if i < 0:
            l,r = 0,n-1
            while l<r:
                self.swap(nums,l,r)
                l+=1
                r-=1
        else:
            kk=n-1
            while nums[kk]<=nums[i]:kk-=1
            self.swap(nums,kk,i)
            l,r = i+1,n-1
            while l<r:
                self.swap(nums,l,r)
                l+=1
                r-=1
    def swap(self,nums,a,b):
        c = nums[a]
        nums[a] = nums[b]
        nums[b] = c
