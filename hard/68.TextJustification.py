"""
思路：理解好题意，一步一步做就可以了
"""


import math


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if maxWidth == 0: return [""]
        n = len(words)
        # print n
        i = 0
        res = []
        while i < n:
            klen = 0
            k = 0
            while klen < maxWidth and i + k < n:
                klen += len(words[i + k]) + 1
                k += 1
            klen -= 1
            r = ''
            #print (i,klen, maxWidth)
            if klen == maxWidth:
                for j in range(k - 1):
                    r += words[i + j] + ' '
                r += words[i + k - 1]
            else:
                if klen>maxWidth:
                    k -= 1
                    klen -= (len(words[i + k]) + 1)
                if i+k>=n:
                    for j in range(k - 1):
                        r += words[i + j] + ' '
                    r += words[i + k - 1]
                    r+=(' '*(maxWidth-len(r)))
                    res.append(r)
                    return res
                #print(k,klen)
                space = maxWidth - klen + k-1
                if k == 1:
                    r += (words[i] + ' ' * space)
                else:
                    for j in range(k - 1):
                        s = math.ceil(float(space) / (k - 1 - j))
                        #print(i, k, s,space)
                        r += (words[i + j] + ' ' * int(s))
                        space -= s

                    r += words[i + k - 1]
            res.append(r)
            i+=k
        return res
                    
                
                
                
                
