class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        l=0
        h=num

        while l<= h:
            m = (l+h) //2
            s = m * m

            if s == num:
                return True
            elif s > num:
                h = m -1
            else:
                l = m + 1
        
        return False