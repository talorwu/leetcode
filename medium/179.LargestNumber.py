"""
sort函数的应用
"""
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        numsStr = [str(x) for x in nums]
        numsStr.sort(cmp = lambda x,y : cmp(x+y,y+x))
        #print numsStr
        numsStr.reverse()
        return ''.join(numsStr).lstrip('0') or '0'
        
            
            
