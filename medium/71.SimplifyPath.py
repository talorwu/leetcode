"""
思路：使用stack
"""
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = [x for x in path.split('/') if x!='.' and x != '']
        stack=[]
        for p in path:
            if p=='..':
                if len(stack)>0:
                    stack.pop()
            else:
                stack.append(p)
        return '/'+'/'.join(stack)
