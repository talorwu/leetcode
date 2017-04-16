class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = s.split(' ')
        tmp.reverse()
        for c in tmp:
            if len(c)!=0:return len(c)
        return 0
