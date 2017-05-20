class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #Approach 1
        # a = [-1]*len(nums)
        # n = len(nums)
        # for i in range(n):
        #     a[(i+k)%n] = nums[i]
        # for i in range(n):
        #     nums[i] = a[i]
            
        #Approach 2
        n = len(nums)
        k = (n+k)%n
        count = 0
        start = -1
        while count < n:
            start += 1 
            pre = nums[start]
            current = start
            flag = False
            while not flag or start != current:
                flag = True
                next = (current + k)%n
                tmp = nums[next]
                nums[next] = pre
                current = next
                pre = tmp
                count += 1
               # print next
        
                
                
                
                
