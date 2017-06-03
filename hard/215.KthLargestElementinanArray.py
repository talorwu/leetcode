class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #min-heap
        
        # heap = []
        # for num in nums:
        #     heapq.heappush(heap,num)
        # for _ in xrange(len(nums)-k):
        #     heapq.heappop(heap)
        # return heapq.heappop(heap)
        
        #quick sort
        return self.findK(nums,len(nums)+1-k)
    
    def findK(self,nums,k):
        if nums:
            pos = self.partition(nums,0,len(nums)-1)
            if k == pos+1:
                return nums[pos]
            elif k < pos+1:
                return self.findK(nums[:pos],k)
            else:
                return self.findK(nums[pos+1:],k-pos-1)
    
    def partition(self,nums,l,r):
        x = (l+r)/2
        nums[x],nums[l] = nums[l],nums[x]
        x = nums[l]
        while l < r:
            while r > l and nums[r] > x:
                r -= 1
            if l < r:
                nums[l] = nums[r]
                l += 1
            while r > l and nums[l] < x:
                l += 1
            if l < r:
                nums[r] = nums[l]
                r -= 1
        nums[l] = x
        return l
            
            
            
            
            
