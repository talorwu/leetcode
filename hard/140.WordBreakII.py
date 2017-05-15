"""
思路：dp+回溯
label[i]记录s[0:i]可以从哪里切割
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        f = [False] * (len(s)+1)
        f[0] = True
        label = [[] for _ in range(len(s)+1)]
        for i in range(1,len(s)+1):
            for j in range(0,i):
                if f[j] and s[j:i] in wordDict:
                    f[i] = True
                    label[i].append(j)
        if label[len(s)]==[]:return []
        result = []
        self.findPath('',result,label,len(s),s)
        return result
        
        
    def findPath(self,res,result,label,step,s):
        if label[step] == []:
            result.append(res[:-1])
            return
        for i in label[step]:
            self.findPath(s[i:step]+' '+res,result,label,i,s)
            
        
        
        
        
        
