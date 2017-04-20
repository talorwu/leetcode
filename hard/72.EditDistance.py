"""
思路：Use f[i][j] to represent the shortest edit distance between word1[0,i) and word2[0, j). Then compare the last character of word1[0,i) and word2[0,j), which are c and d respectively (c == word1[i-1], d == word2[j-1]):

if c == d, then : f[i][j] = f[i-1][j-1]

Otherwise we can use three operations to convert word1 to word2:

(a) if we replaced c with d: f[i][j] = f[i-1][j-1] + 1;

(b) if we added d after c: f[i][j] = f[i][j-1] + 1;

(c) if we deleted c: f[i][j] = f[i-1][j] + 1;

因为计算f[i][j]时只用了前一行元素和上一个计算的元素，因此可以只用两行数组，循环计算
注意：使用一行也是可以的，麻烦一点，需要记录前一个计算的f[i,j-1],推迟更新
参考：
for (int i = 1; i <= l1; ++i)
        {
            int prev = i;
            for (int j = 1; j <= l2; ++j)
            {
                int cur;
                if (word1[i-1] == word2[j-1]) {
                    cur = f[j-1];
                } else {
                    cur = min(min(f[j-1], prev), f[j]) + 1;
                }
    
                f[j-1] = prev;
                prev = cur;
            }
            f[l2] = prev;
        }

"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        if m==0:return n
        if n==0:return m
        f = [[0]*(n+1) for _ in range(2)]
        for i in range(n+1):
            f[0][i] = i
        f[1][0] = 1
        for i in range(1,m+1):
            f[i%2][0]=i
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    f[i%2][j] = f[(i-1)%2][j-1]
                else :
                    f[i%2][j] = min(min(f[(i-1)%2][j-1],f[(i)%2][j-1]),f[(i-1)%2][j])+1
            #print f
        
        return f[m%2][n]
                
        
