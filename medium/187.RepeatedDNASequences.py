class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        Hash = {}
        if len(s) <= 10:return res
        for i in range(len(s)-9):
            if s[i:i+10] not in Hash:
                Hash[s[i:i+10]] = 1
            else:
                Hash[s[i:i+10]] += 1
        #print Hash
        for h in Hash:
            if Hash[h] >= 2:
                res.append(h)
        return res
