"""
 思路，贪心算法，观察字符串，a(0)a(1)a(2)...a(i)...a(n)a(n+1)，假设从a(0)开始的到a(n+1)停止，说明a(0)到a(n)有一个与a(n+1)相同，设为a(i),则a(0)到a(i-1)的substring必小于从a(0)开始的，因此下一次可以从a(i+1)开始，因此需要记住a(i)的下标，使用hash记录所有使用过的字符就可以了
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = start = 0
        usedchar = {}
        for i in range(len(s)):
            if s[i] in usedchar and start <= usedchar[s[i]]:
                start = usedchar[s[i]] + 1
            else:
                maxlen = max(maxlen , i - start + 1)
            usedchar[s[i]] = i
        return maxlen
            
