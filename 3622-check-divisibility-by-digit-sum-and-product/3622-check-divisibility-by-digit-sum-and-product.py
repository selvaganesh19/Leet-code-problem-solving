class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        sum = 0
        pro=1
        t = n

        while t >0:
            r = t % 10
            sum+=r
            pro*=r
            t//=10
        
        if n % (sum+pro) == 0:
            return True
        else:
            return False