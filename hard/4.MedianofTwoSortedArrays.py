#题解看https://discuss.leetcode.com/topic/4996/share-my-o-log-min-m-n-solution-with-explanation
"""
思路：要找到两个数组的中间数，需要满足两个条件，假设对于A，B 分别以i，j分割
      left_part          |        right_part
A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]

只要满足两个条件：1.left_part和right_part长度一样
		 2.left_part全部小于right_part
中间值为(max(left_part)+min(right_part))/2
于是可以另i = 0~m , j = (m+n+1)/2 - i ;st. m = len(A),n = len(B),且m<=n
到这里可以利用二分查找了，如果A[i-1]>B[j] ,i需要变小，如果B[j-1]>A[i]，i需要增大

"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m,n,A,B = len(nums1),len(nums2),nums1,nums2
        if m > n:
            m,n,A,B = n,m,nums2,nums1
        imin = 0
        imax = m
        while imin <= imax:
            i = (imin+imax)/2
            j = (m+n+1)/2-i
            if i>0 and A[i-1] > B[j]:
                imax = i-1
            elif i<m and B[j-1] > A[i]:
                imin = i+1
            else:
                if i==0:max_left = B[j-1]
                elif j==0:max_left = A[i-1]
                else: max_left = max(A[i-1],B[j-1])
                
                
                if (m+n)%2:
                    return max_left
                if i==m:min_right = B[j]
                elif j==n:min_right = A[i]
                else: min_right = min(A[i],B[j])
                
                return (max_left + min_right)/2.0
        
        


