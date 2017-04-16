"""
思路：对intervals按照start排序
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals,key = lambda x:x.start)
        results = []
        for i in range(len(intervals)):
            if len(results)==0 or intervals[i].start > results[-1].end:
                tmp = Interval(intervals[i].start,intervals[i].end)
                results.append(tmp)
            else:
                results[-1].end = max(intervals[i].end,results[-1].end)
        return results
        
