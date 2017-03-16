"""
思路：从两边开始，l表示左边，r表示右边，if height[l] <= height[r]:l++，否则r--
证明，假设height[l] <= height[r]，则我们舍弃了（l,l+1）...（l,r-1），所有的这些桶子，高度都小于等于height[l]，宽度小于（l，r）,所以他们都会小于(l,r)桶子
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        '''
         Time Limit Exceeded 
         ##
         
        maxWater = 0
        for i in range(len(height)):
            for j in range(i):
                maxWater = max(maxWater,min(height[i],height[j])*(i-j))
        return maxWater
        '''
        l = 0;r = len(height)-1
        maxWater= 0
        while(l<r):
            maxWater = max(maxWater,min(height[l],height[r])*(r-l))
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1
        return maxWater
                    
