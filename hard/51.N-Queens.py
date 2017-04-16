"""
思路：DFS，题目本身不难，但是有一个点
a = [1,2]
    b = [3,4]
    c=[]
    c.append(a)
    c.append(b)
    a[0] = 5
    print(c)

c = [[5,2],[3,4]]!!!!
即append也只是加入的地址而已

"""
import copy
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        results = []
        res = ['.'*n]*n
        self.DFS(0,n,[],res,results)
        #print res
        return results
        
    def DFS(self,step,n,Q_loc,res,results):
        if step == n:
            tmp = copy.deepcopy(res)
            results.append(tmp)
            #print res
            return 
        
        for i in range(n):
            res[step] = res[step][:i]+'Q'+res[step][i+1:]
            Q_loc.append((step,i))
            #print step,i,res
            if self.check(Q_loc):
                self.DFS(step+1,n,Q_loc,res,results)
            res[step] = res[step][:i]+'.'+res[step][i+1:]
            Q_loc.remove((step,i))
    def check(self,loc):
        Len=len(loc)
        tmp=[-1]*Len
        for i in range(Len):
            tmp[loc[i][0]] = loc[i][1]
        
        for i in range(Len-1):
            if tmp[i] == tmp[Len-1] or abs(Len-1-i) == abs(tmp[Len-1]-tmp[i]):return False
        return True
            
        
