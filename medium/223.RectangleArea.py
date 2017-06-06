"""
http://www.jianshu.com/p/59e841a8671c
"""
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        MaxArea = (C-A)*(D-B)+(G-E)*(H-F)
        if E >= C or F >= D or B >= H or G <= A:
            return MaxArea
        left = max(A,E)
        right = min(C,G)
        top = min(D,H)
        bottom = max(B,F)
        return MaxArea - (right-left)*(top-bottom)
