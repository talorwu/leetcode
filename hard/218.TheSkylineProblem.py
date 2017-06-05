"""
思路：
"""

from heapq import *

class Solution:
    def getSkyline(self, buildings):
        skyline = []
        i, n = 0, len(buildings)
        liveHR = []
        while i < n or liveHR:
            if not liveHR or i < n and buildings[i][0] <= -liveHR[0][1]:
                x = buildings[i][0]
                while i < n and buildings[i][0] == x:
                    heappush(liveHR, (-buildings[i][2], -buildings[i][1]))
                    i += 1
            else:
                x = -liveHR[0][1]
                while liveHR and -liveHR[0][1] <= x:
                    heappop(liveHR)
            height = len(liveHR) and -liveHR[0][0]
            if not skyline or height != skyline[-1][1]:
                skyline += [x, height],
        return skyline
