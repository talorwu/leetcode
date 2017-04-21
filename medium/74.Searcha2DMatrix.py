"""
思路：两次二分查找，第一次查找在哪一行，第二次某一行查找元素
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        if n==0:return False
        m = len(matrix[0])
        if m==0:return False
        l,r,row=0,n-1,-1
        while l<=r:
            mid = (l+r)/2
            if matrix[mid][0]<=target and (mid+1>r or matrix[mid+1][0]>target):
                row=mid
                break
            elif matrix[mid][0]>target:
                r = mid-1
            else:
                l = mid+1
        l,r=0,m-1
        if row==-1:return False
        while l<=r:
            mid = (l+r)/2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]>target:
                r = mid -1
            else:
                l = mid+1
        return False
            
            
            
            
            
