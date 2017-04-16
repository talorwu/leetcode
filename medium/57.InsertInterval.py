# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals)==0:return [newInterval]
        results = []
        i=0
        flag = False
        while i < len(intervals):
            if intervals[i].start > newInterval.start:
                flag = True
                if len(results)==0 or newInterval.start > results[-1].end:
                    tmp = Interval(newInterval.start,newInterval.end)
                    results.append(tmp)
                else:
                    results[-1].end = max(results[-1].end,newInterval.end)
            if len(results)==0 or intervals[i].start > results[-1].end:
                tmp = Interval(intervals[i].start,intervals[i].end)
                results.append(tmp)
            else:
                results[-1].end = max(intervals[i].end,results[-1].end)
            i+=1
        if not flag:
            if len(results)==0 or newInterval.start > results[-1].end:
                tmp = Interval(newInterval.start,newInterval.end)
                results.append(tmp)
            else:
                results[-1].end = max(results[-1].end,newInterval.end)
        return results
                
        
