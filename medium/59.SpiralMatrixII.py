class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix =  [[0] * n for _ in range(n)]
        rowBegin,rowEnd,colBegin,colEnd = 0,n-1,0,n-1
        k = 1
        while rowBegin<=rowEnd and colBegin<=colEnd:
            #print matrix
            for i in range(colBegin,colEnd+1):
                matrix[rowBegin][i] = k
                k+=1
            rowBegin+=1
            for i in range(rowBegin,rowEnd+1):
                matrix[i][colEnd] = k
                k+=1
            colEnd-=1
            for i in range(colBegin,colEnd+1)[::-1]:
                matrix[rowEnd][i] = k
                k+=1
            rowEnd-=1
            for i in range(rowBegin,rowEnd+1)[::-1]:
                matrix[i][colBegin] = k
                k+=1
            colBegin+=1
        return matrix
            
