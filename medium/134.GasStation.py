"""
思路：经典题
证明  https://discuss.leetcode.com/topic/39755/proof-of-if-total-gas-is-greater-than-total-cost-there-is-a-solution-c
"""

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total = 0
        start = 0
        remain = 0
        for i in range(len(gas)):
            remain += gas[i]-cost[i]
            total += gas[i] - cost[i]
            if remain < 0:
                start = i+1
                remain = 0
                
        if total < 0:return -1
        else: return start 
