class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        nums1 = [int(v) for v in version1.split('.')]
        nums2 = [int(v) for v in version2.split('.')]
        a=[1,2]
        b = [2,3]
        for i in range(min(len(nums1),len(nums2))):
            if nums1[i] < nums2[i]:return -1
            if nums1[i] > nums2[i]:return 1
        if sum(nums1) == sum(nums2):return 0
        if len(nums1) < len(nums2):return -1
        elif len(nums1) > len(nums2):return 1
        return 0
