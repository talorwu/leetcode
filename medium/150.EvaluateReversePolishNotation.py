"""
思路：stack
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        a = ['+','-','*','/']
        for c in tokens:
            if c in a:
                x1 = stack.pop()
                x2 = stack.pop()
                ans = self.cal(x2,x1,c)
                #print x2,x1,ans
                stack.append(ans)
            else:
                stack.append(c)
        return int(stack.pop())
        
    def cal(self,a,b,c):
        if c == '+':
            return str(int(a)+int(b))
        if c == '-':
            return str(int(a)-int(b))
        if c == '*':
            return str(int(a)*int(b))
        if c == '/':
            if int(a)*int(b) < 0 and int(a) % int(b)  != 0:
                return str(int(a)/int(b) + 1)
            return str(int(a)/int(b))
        
        
        
        
        
        
        
        
        
