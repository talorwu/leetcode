"""
思路：先将words转成dict，然后设置一个m×k的窗口，看窗口内的字符串是否匹配
"""

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        word_dict = {}
        k = len(words)
        m = len(words[0])
        n = len(s)
        ans = []
        #转成dict
        for c in words:
            if c not in word_dict:
                word_dict[c] = 1
            else:word_dict[c]+=1
        for i in range(n-m*k+1):
            l,r = i,i+m*(k-1)
            tmp = {}
            while l<=r:
                str1 = s[l:l+m]
                #print(i,l,str1)
                if str1 in word_dict:
                    tmp[str1]=tmp[str1]+1 if str1 in tmp else 1
                    if tmp[str1] > word_dict[str1]:
                        break
                else:break
                l+=m
            if l > r:ans.append(i)
        return ans
                
            
            
            
