"""
思路1：f(n)表示n的时候的全括号匹配，f(n) = ()f(n-1) or f(n-1)() or (f(n-1)),'()()()...()()'特殊处理，这种方法实际是错误的，因为无法解决()f(n-1) == f(n-1)()的情况，而且对于n=4时，(())(())无法产生
思路2：深度优先搜索
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        if n==1:
            res.append("()")
            return res
        else:
            resfront = self.generateParenthesis(n-1)
            res.append(resfront[0]+"()")
            res.append("("+resfront[0]+")")
            for c in resfront[1:]:
                res.append("()"+c)
                res.append(c+"()")
                res.append("("+c+")")
        return res


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        List = []
        self.DFS("",List,0,0,n)
        return List
        
    def DFS(self,res,List,left,right,n):
        if len(res)==n*2:
            List.append(res)
        else:
            if left < n:
                self.DFS(res+'(' , List,left+1,right,n)
            if right < left:
                self.DFS(res+')' , List,left,right+1,n)
        
                
        
            
            


            
