class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:return 0
        n = len(nums)
        res = 0
        for i in range(n):
            flag = [False]*n
            f = [0]*len(nums)
            f[0] = nums[i]
            flag[0] = True
            if n == 1:return f[0]
            f[1] = max(nums[i],nums[(i+1)%n])
            if nums[i] > nums[(i+1)%n]:
                flag[1] = True
            for j in range(2,n):
                if f[j-1] > f[j-2]+nums[(j+i)%n]:
                    flag[j] = flag[j-1]
                else:
                    flag[j] = flag[j-2]
                if j == n-1 and flag[j]:
                    f[j] = f[j-1]
                    continue
                f[j] = max(f[j-1],f[j-2]+nums[(j+i)%n])
                
            res = max(res,f[-1])
        return res

"""
分两种情况，1.nums[0]可能取，2.nums[n-1]可能取
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==0:return 0
        if n==1:return nums[0]
        return max(self.rob1(nums,0,n-1),self.rob1(nums,1,n))
    def rob1(self, nums,i,j):
        """
        :type nums: List[int]
        :rtype: int
        """
        if i+1 ==j:return nums[i]
        n = len(nums)-1
        if n == 0:return 0
        pre = nums[i]
        if n == 1:return pre
        cur = max(nums[i],nums[i+1])
        for k in range(2+i,j):
            tmp = cur
            cur = max(cur,pre+nums[k])
            pre = tmp
        return cur   
