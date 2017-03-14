"""
方法一：找规律，第一行和最后一行元素减半，中间的元素多，循环为2(numRows-1)
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = []
        slist = list(s)
        #print(slist)
        n = len(s)
        if numRows == 1:
            return s
        for i in xrange(numRows):
            if i==0:
                tmp = 0
                while tmp < n:
                    res.append(slist[tmp])
                    tmp += 2*(numRows-1)
            elif i < numRows-1:
                
                tmp = tmp1 = i
                tmp2 = 2*(numRows - 1)-i
                flag = 0
                while tmp < n:
                    if flag%2 :
                        res.append(slist[tmp2])
                        tmp2+=2*(numRows-1)
                        tmp = tmp1
                        flag = 0
                    else:
                        res.append(slist[tmp1])
                        tmp1+=2*(numRows-1)
                        tmp = tmp2
                        flag = 1
            else:
                tmp = numRows-1
                while tmp < n:
                    res.append(slist[tmp])
                    tmp+=2*(numRows-1)
        #print(res)
        return "".join(res)

"""
方法二： L = [''] * numRows，L[i]代表第i行的字符串，碰到0和numRows-1掉头
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)
