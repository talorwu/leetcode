

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:return 0
        prime = [True]*n
        prime[0] = prime[1] = False
        for i in range(2,int(n**0.5)+1):
            if prime[i]:
                prime[i*i:n:i] = [False]*len(prime[i*i:n:i])
        return sum(prime)
