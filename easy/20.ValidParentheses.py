"""
思路：stack的应用
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        tmp = {')':'(',']':'[','}':'{'}
        for c in s:
            if c in tmp.values():
                stack.append(c)
            else:
                if len(stack) == 0 or stack.pop() != tmp[c]:
                    return False
        return len(stack)==0

        
        
