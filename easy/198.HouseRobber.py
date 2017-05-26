"""
DP:f[i]表示nums[0:i+1]的最大值，f[i] = max(f[i-1],f[i-2]+nums[i])
	f[i-1]表示nums[i]不取，f[i-2]+nums[i]表示取nums[i],为什么取nums[i]的时候是f[i-2]+nums[i],f[i-1]也可能nums[i-1]不取，这时候不是可以取nums[i]吗？
     	因为如果f[i-1]不取nums[i-1]，按照递推公式则f[i-1] = f[i-2]的，所以这时候f[i] = f[i-1]+nums[i] = f[i-2]+nums[i],另外如果f[i-1]取了nums[i-1]则只能
  	f[i] = f[i-2]+nums[i]了
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:return 0
        f = [0]*n
        f[0] = nums[0]
        if n == 1:return f[0]
        f[1] = max(nums[0],nums[1])
        for i in range(2,n):
            f[i] = max(f[i-1],f[i-2]+nums[i])
        return f[-1]
