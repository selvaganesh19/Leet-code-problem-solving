class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def add(n):
            if n < 10:  
                return n
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return add(s)   
        
        return add(num)
