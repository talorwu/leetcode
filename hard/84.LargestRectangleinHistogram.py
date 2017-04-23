"""
思路：
使用stack，stack存下标值，存上升的下标值，遇见下降的时候开始计算ans，并讲大于新heights的元素出栈
"""

class Solution(object):
    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in xrange(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
            #print stack
        height.pop()
        return ans
        
