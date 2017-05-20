class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
	#python 简单解法
        #return int(bin(n)[2:].zfill(32)[::-1],2)
        res = 0
        for i in range(32):
            res <<= 1
            res |= n&1
            n>>=1
        return res
