"""
思路：记录s中出现的t中每一个字母的下标,当全部匹配完以后开始更新start和end，当匹配的新字母时，更新该字母的下标
举个例子：
s: ADOBECODEBANAABC
t: ACBA

A:[0,10,12,13]
B:[3,9,14]
C:[5,15]

当匹配到s[10]时，A:[0,10],B:[9],C:[5]，这是没有miss了，所以区间为[0,10]
当匹配到s[12]时，A:[10,12],B[9],C:[5],这是没有miss了，所以区间为[5,12]
当匹配到s[13]时，A:[12,13],B[9],C:[5],这是没有miss了，所以区间为[5,13]
当匹配到s[14]时，A:[12,13],B[14],C:[5],这是没有miss了，所以区间为[5,14]
当匹配到s[12]时，A:[12,13],B[14],C:[15],这是没有miss了，所以区间为[12,15]

"""


class Solution(object):
    def minWindow(self, s, t):
        indices = {}
        for c in t:
            indices[c]=[]
        miss = list(t)
        start,end = 0,len(s)
        for i in range(len(s)):
            if s[i] in t:
                indices[s[i]].append(i)
                if s[i] in miss:
                    miss.remove(s[i])
                else:
                    indices[s[i]].pop(0)
            if miss == []:
                right = max(x[-1] for x in indices.values())
                left = min(x[0] for x in indices.values())
                if right-left<end-start:
                    start = left
                    end = right
            #print miss,indices
        if miss!=[]:
            return ""
        else:
            return s[start:end+1]
                
