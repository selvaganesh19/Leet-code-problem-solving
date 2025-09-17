import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <=2:
            return 0

        
        res = [True] * n
        res[0] = res[1] = False

        i=2

        while i * i < n:
            if res[i]:
                for j in range(i*i,n,i):
                    res[j]=False
                
            i+=1
        
        return sum(res)