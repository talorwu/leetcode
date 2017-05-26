class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashs = {}
        hasht = {}
        for i in range(len(s)):
            if s[i] in hashs:
                if t[i] in hasht:
                    if hashs[s[i]] == hasht[t[i]]:
                        hashs[s[i]] = i
                        hasht[t[i]] = i
                    else:
                        return False
                else:
                    return False
            elif t[i] in hasht:return False
            else:
                hashs[s[i]] = i
                hasht[t[i]] = i
        return True
